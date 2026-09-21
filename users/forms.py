from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "email",
            "password1",
            "password2"
        )
