# Generated by Django 3.0.5 on 2020-05-10 22:46

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
