# Generated by Django 3.0.5 on 2020-05-17 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_transactionalemail_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionalemail',
            name='body',
        ),
    ]
