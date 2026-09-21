from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "users/signup.html"