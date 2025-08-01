"""
URL configuration for userHelp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', reg.registeruser, name="register"),
    path("", include("userHelpApp.urls")) #whenever I go to this empty string it will go: EX= if we have "MAIN" to access website we have to use MAIN/(what is in urls.py whihc right now is "")
]
