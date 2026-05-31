from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [
    # Public
    path('', views.tree_view, name='tree_view'),
    path('person/<int:pk>/', views.person_detail_htmx, name='person_detail'),

    # Admin panel
    path('tree/admin/login/', views.admin_login_view, name='admin_login'),
    path('tree/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('tree/admin/person/add/', views.admin_add_person, name='admin_add_person'),
    path('tree/admin/person/<int:pk>/edit/', views.admin_edit_person, name='admin_edit_person'),
    path('tree/admin/person/<int:pk>/delete/', views.admin_delete_person, name='admin_delete_person'),
    path('tree/admin/logout/', views.admin_logout_view, name='admin_logout'),
]
