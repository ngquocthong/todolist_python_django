from importlib.resources import path

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="name"),
]