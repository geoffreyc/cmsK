from django.db import models
from django.contrib.auth.models import User


# User profile
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here


# Categories model
class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


# Posts model
class Post(models.Model):
    title = models.TextField()
    slug = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User)
    keywords = models.TextField(blank=True, null=True)
    date_create = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)