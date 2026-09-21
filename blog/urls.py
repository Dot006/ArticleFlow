from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(route='',
         view=views.HomePageTemplateView.as_view(),
         name='homepage'),
]
