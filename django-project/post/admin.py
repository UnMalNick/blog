from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                ('is_draft', 'is_active'),
                ('author', 'category'),
                'seo_title',
                'seo_description',
                'body'
            ),
        }),
    )

    change_form_template = 'admin/custom/change_form.html'

admin.site.register(models.PostCategory)
admin.site.register(models.Post, PostAdmin)