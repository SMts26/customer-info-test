from django import forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #Pre built form that will help set up the user
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): #This will take the atributes from UserCreationForm
    email = forms.EmailField()
    class Meta: #We need it to save to the users DB
        model = User #we gonna change the user form
        fields = ['username', 'email', 'password1', 'password2'] #This will lay out where we want the fields to be
