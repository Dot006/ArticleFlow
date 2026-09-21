from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path(route='signup/',
         view=views.SignUpView.as_view(),
         name='signup'),
]
