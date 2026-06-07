from django.contrib import admin
from .models import Person, Relationship

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display  = ("full_name", "gender", "birth_date", "death_date")
    search_fields = ("first_name", "last_name")

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display  = ("from_person", "rel_type", "to_person")
    list_filter   = ("rel_type",)
