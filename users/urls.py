from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path(route='signup/',
         view=views.SignUpView.as_view(),
         name='signup'),
    path(route='login/',
         view=views.UserLoginView.as_view(),
         name='login'),
]
