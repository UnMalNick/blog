from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from mail.models import TransactionalEmail, EmailToUser


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        try:
            email = TransactionalEmail.objects.get(slug='welcome')
        except TransactionalEmail.DoesNotExist:
            email = False

        if email:
            create_email = EmailToUser.objects.create(
                email=email,
                user=instance
            )
            create_email.save()