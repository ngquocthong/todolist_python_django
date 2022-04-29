from importlib.resources import path

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("create/", views.create, name="create"),
]