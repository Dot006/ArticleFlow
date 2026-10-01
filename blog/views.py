from django.shortcuts import render
from django.views.generic import ListView
from . import models

class HomePageTemplateView(ListView):
    model = models.Article
    template_name = "homepage.html"
    context_object_name = "articles" # default is article_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["recentArticles"] = models.Article.objects.all().order_by("-published_at").values()[:5]
        return context
    
    
    