from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailToUser
from .tasks import send_email

@receiver(post_save, sender=EmailToUser)
def create_task_send_email(sender, instance, created, **kwargs):
    if created and instance.status == 'dj-waiting':
        send_email.delay(instance.id)