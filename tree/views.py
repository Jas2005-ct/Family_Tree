from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django_htmx.http import trigger_client_event
from .models import Person
from .forms import PersonForm
import json


def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# ─── Public Views ──────────────────────────────────────────────

def tree_view(request):
    """Main family tree page"""
    persons = Person.objects.all().order_by('generation', 'id')

    # Build tree data for JS
    tree_data = []
    for p in persons:
        tree_data.append({
            'id': p.id,
            'name': p.name,
            'role': p.role,
            'generation': p.generation,
            'gender': p.gender,
            'birth_year': p.birth_year,
            'is_alive': p.is_alive,
            'parent_id': p.parent_id,
            'spouse_id': p.spouse_id,
            'photo': p.get_photo(),
            'notes': p.notes,
        })

    context = {
        'persons': persons,
        'tree_data_json': json.dumps(tree_data),
        'total_members': persons.count(),
        'generations': persons.values_list('generation', flat=True).distinct().order_by('generation'),
    }
    return render(request, 'tree/tree.html', context)


def person_detail_htmx(request, pk):
    """HTMX: Load person detail card"""
    person = get_object_or_404(Person, pk=pk)
    children = person.get_children()
    siblings = person.get_siblings()
    return render(request, 'tree/partials/person_card.html', {
        'person': person,
        'children': children,
        'siblings': siblings,
    })


# ─── Admin Views ───────────────────────────────────────────────

def admin_login_view(request):
    if request.user.is_authenticated and is_admin(request.user):
        return redirect('tree:admin_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and is_admin(user):
            login(request, user)
            return redirect('tree:admin_dashboard')
        messages.error(request, 'Invalid credentials or insufficient permissions.')
    return render(request, 'tree/admin/login.html')


@login_required(login_url='/tree/admin/login/')
@user_passes_test(is_admin, login_url='/tree/admin/login/')
def admin_dashboard(request):
    persons = Person.objects.all().order_by('generation', 'name')
    context = {
        'persons': persons,
        'total': persons.count(),
        'gen_counts': {
            1: persons.filter(generation=1).count(),
            2: persons.filter(generation=2).count(),
            3: persons.filter(generation=3).count(),
        }
    }
    return render(request, 'tree/admin/dashboard.html', context)


@login_required(login_url='/tree/admin/login/')
@user_passes_test(is_admin, login_url='/tree/admin/login/')
def admin_add_person(request):
    """Add person - supports HTMX partial + full page"""
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save()
            if request.htmx:
                response = render(request, 'tree/partials/person_row.html', {'person': person})
                trigger_client_event(response, 'personAdded', {})
                return response
            messages.success(request, f'✅ {person.name} added successfully!')
            return redirect('tree:admin_dashboard')
        else:
            if request.htmx:
                return render(request, 'tree/partials/add_person_form.html', {'form': form})
    else:
        form = PersonForm()

    if request.htmx:
        return render(request, 'tree/partials/add_person_form.html', {'form': form})
    return render(request, 'tree/admin/add_person.html', {'form': form})


@login_required(login_url='/tree/admin/login/')
@user_passes_test(is_admin, login_url='/tree/admin/login/')
def admin_edit_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            if request.htmx:
                return render(request, 'tree/partials/person_row.html', {'person': person})
            messages.success(request, f'✅ {person.name} updated!')
            return redirect('tree:admin_dashboard')
    else:
        form = PersonForm(instance=person)

    if request.htmx:
        return render(request, 'tree/partials/edit_person_form.html', {'form': form, 'person': person})
    return render(request, 'tree/admin/edit_person.html', {'form': form, 'person': person})


@login_required(login_url='/tree/admin/login/')
@user_passes_test(is_admin, login_url='/tree/admin/login/')
def admin_delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        name = person.name
        person.delete()
        if request.htmx:
            response = HttpResponse('')
            trigger_client_event(response, 'personDeleted', {})
            return response
        messages.success(request, f'🗑️ {name} removed.')
        return redirect('tree:admin_dashboard')
    return render(request, 'tree/admin/confirm_delete.html', {'person': person})


def admin_logout_view(request):
    logout(request)
    return redirect('tree:tree_view')
