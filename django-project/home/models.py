from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class TermsOfService(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    body = FroalaField()


class Privacy(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    body = FroalaField()