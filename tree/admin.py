from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'generation', 'gender', 'birth_year', 'is_alive', 'parent', 'spouse']
    list_filter = ['generation', 'role', 'gender', 'is_alive']
    search_fields = ['name', 'notes']
    ordering = ['generation', 'name']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'gender', 'generation', 'role', 'birth_year', 'birth_date', 'is_alive')
        }),
        ('Photo', {
            'fields': ('photo', 'photo_url'),
            'classes': ('collapse',)
        }),
        ('Relationships', {
            'fields': ('parent', 'spouse')
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
