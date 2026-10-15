from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:login")
    
class UserLoginView(LoginView):
    template_name = "users/login.html"
    next_page = "/"
    redirect_authenticated_user = True
    
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('blog:homepage')
    