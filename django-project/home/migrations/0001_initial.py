# Generated by Django 3.0.5 on 2020-05-10 22:46

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('body', froala_editor.fields.FroalaField()),
            ],
        ),
        migrations.CreateModel(
            name='TermsOfService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('body', froala_editor.fields.FroalaField()),
            ],
        ),
    ]
