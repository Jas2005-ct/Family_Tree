from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"persons",       views.PersonViewSet,       basename="person")
router.register(r"relationships", views.RelationshipViewSet, basename="relationship")

urlpatterns = [
    path("",        views.tree_view, name="tree"),
    path("api/v1/", include(router.urls)),
]
