from typing import Any

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from .utils import render_markdown, markdown_to_plain_text

class HomePageView(ListView):
    model = models.Article
    template_name = "homepage.html"
    context_object_name = "articles" # default is article_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["recentArticles"] = models.Article.objects.all().order_by("-published_at").values()[:5]
        for article in context["articles"]:
            article.preview = markdown_to_plain_text(article.content)
        return context

class ArticleDetailView(DetailView):
    model = models.Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["recentArticles"] = models.Article.objects.all().order_by("-published_at").values()[:5]
        context['content_html'] = render_markdown(self.object.content)
        return context
    
    