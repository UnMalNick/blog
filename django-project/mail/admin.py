from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Sender)
admin.site.register(models.TransactionalEmail)
admin.site.register(models.EmailToUser)