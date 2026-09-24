from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = AutoSlugField("Category Address",
                         unique=True, populate_from="name", always_update=False)
    def __str__(self):
        return self.name
    