from rest_framework import serializers
from .models import Person, Relationship


class PersonSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model  = Person
        fields = "__all__"


class RelationshipSerializer(serializers.ModelSerializer):
    from_name = serializers.SerializerMethodField()
    to_name   = serializers.SerializerMethodField()

    class Meta:
        model  = Relationship
        fields = "__all__"

    def get_from_name(self, obj):
        return obj.from_person.full_name

    def get_to_name(self, obj):
        return obj.to_person.full_name
