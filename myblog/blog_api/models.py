# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Defines a blog category
    """

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Defines a blog article
    """

    writer = models.ForeignKey(User, related_name="articles")
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name="articles")
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.content
