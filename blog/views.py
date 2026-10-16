from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
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
    def get_queryset(self):
        queryset = models.Article.objects.filter(status='published')
        query = self.request.GET.get("search", "").strip()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

class ArticleDetailView(DetailView):
    model = models.Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["recentArticles"] = models.Article.objects.all().order_by("-published_at").values()[:5]
        context['content_html'] = render_markdown(self.object.content)
        context['comments'] = self.object.comments.select_related('author').order_by('-created')
        return context

class CategoryArticlesView(DetailView):
    model = models.Category
    template_name = 'blog/category_articles.html'
    context_object_name = 'categories'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["recentArticles"] = models.Article.objects.all().order_by("-published_at").values()[:5]
        context["articles"] = self.object.articles.filter(status='published')
        for article in context["articles"]:
            article.preview = markdown_to_plain_text(article.content)
        return context
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ['content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(models.Article, slug=self.kwargs['slug'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog:article-detail', kwargs={"slug": self.kwargs["slug"]})
    login_url = 'users:login'    
