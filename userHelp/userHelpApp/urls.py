from django.urls import path, include
from . import views

urlpatterns = [
    path("new/", views.addItem, name="newItem")
]
