from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from orak.models import student


class studentCreationForm(UserCreationForm):
    class Meta:
        model = student
        fields = ['username', 'email', 'password1', 'password2']