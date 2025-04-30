from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/", include([
        path("new/", views.addItem, name="newItem")
    ]))
]