from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("cinemahall/", cinemahall_list, name="cinemahall-list"),
    path("cinemahall/<int:pk>/", cinemahall_detail, name="cinemahall-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>", ActorDetail.as_view(), name="actor-detail"),
    path("genre", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>", GenreDetail.as_view(), name="genre-detail")
]

app_name = "cinema"
