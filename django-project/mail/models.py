from django.db import models
from froala_editor.fields import FroalaField

from django.contrib.auth.models import User
# Create your models here.


class Sender(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TransactionalEmail(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    

class EmailToUser(models.Model):
    STATUS_CHOICES = [
        ('dj-waiting', 'Waiting On Celery'),
        ('sent', 'Mandrill - Sent'),
        ('queued', 'Mandrill - En Cola'),
        ('scheduled', 'Mandrill - Agendado'),
        ('rejected', 'Mandrill - Rechazado'),
        ('invalid', 'Mandrill - Invalido'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(TransactionalEmail, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='dj-waiting')
    reject_reason = models.CharField(max_length=200, blank=True, null=True)
    message_id = models.CharField(max_length=200, blank=True, null=True)