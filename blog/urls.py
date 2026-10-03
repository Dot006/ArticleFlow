from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(route='',
         view=views.HomePageView.as_view(),
         name='homepage'),
    path(route='articles/<slug:slug>/',
         view=views.ArticleDetailView.as_view(),
         name='article-detail'),
    path(route='categories/<slug:slug>/',
         view=views.CategoryArticlesView.as_view(),
         name='categoryArticles'),
    
]
