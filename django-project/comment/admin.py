from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    change_form_template = 'admin/custom/change_form.html'

# Register your models here.
admin.site.register(models.Comment, CommentAdmin)