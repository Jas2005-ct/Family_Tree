from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Person, Relationship
from .serializers import PersonSerializer, RelationshipSerializer


def tree_view(request):
    return render(request, "tree/index.html")


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("birth_date")
    serializer_class = PersonSerializer

    @action(detail=False, methods=["get"], url_path="graph-data")
    def graph_data(self, request):
        """Returns {nodes, links} payload for D3.js."""
        persons = Person.objects.all()
        rels    = Relationship.objects.select_related("from_person", "to_person").all()

        nodes = [
            {
                "id":     p.id,
                "name":   p.full_name,
                "gender": p.gender,
                "birth":  str(p.birth_date) if p.birth_date else None,
                "photo":  request.build_absolute_uri(p.photo.url) if p.photo else None,
            }
            for p in persons
        ]

        links = [
            {
                "source":   r.from_person_id,
                "target":   r.to_person_id,
                "rel_type": r.rel_type,
            }
            for r in rels
        ]

        return Response({"nodes": nodes, "links": links})


class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.select_related("from_person", "to_person").all()
    serializer_class = RelationshipSerializer
