from django.contrib import admin  # noqa

from .models import News, Comment

admin.site.register(News)
admin.site.register(Comment)
