from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): #Inherits from user creation form
    email = forms.EmailField()

    class Meta: #Nested namespace for configurations
        model = User #Model that will be affected
        fields = ['username', 'email', 'password1', 'password2'] #Fields that we want in the form

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: #Nested namespace for configurations
        model = User #Model that will be affected
        fields = ['username', 'email'] #Fields that we want in the form

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']