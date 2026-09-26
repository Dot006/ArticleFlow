from django.conf import settings
from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

class Category(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = AutoSlugField("Category Address",
                         unique=True, populate_from="name", always_update=False)
    def __str__(self):
        return self.name

class Article(TimeStampedModel, StatusModel):
    title = models.CharField(("Title"), max_length=50)
    content = models.TextField(("Content"))
    slug = AutoSlugField("Article Address",
                         unique=True, populate_from="title", always_update=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE
    )
    STATUS = Choices('draft', 'published')
    published_at = models.DateTimeField("published", null=True, blank=True)
    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
    )
    
    
    
