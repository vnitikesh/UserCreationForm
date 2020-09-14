from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.CharField(max_length = 200, required = False, widget = forms.EmailInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
