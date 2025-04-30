from django.urls import path, include
from register import views as reg
from userHelpApp import views as uha

urlpatterns = [
    path("", include([
        path("register/", reg.registeruser, name="register"),
        path("", include([
            path("", include("django.contrib.auth.urls"), name="login")
        ])),
        path("login/", include([
                path("register/", reg.registeruser, name="register")
        ]))
    ]))
]