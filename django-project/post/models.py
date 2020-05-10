from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
# Create your models here.


class PostCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True, null=True)
    seo_title = models.CharField(max_length=60)
    seo_description = models.TextField(max_length=160)
    body = FroalaField()
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)