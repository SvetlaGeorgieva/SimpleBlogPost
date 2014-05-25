from django.contrib import admin
from .models import Article, Mood


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

    list_display_links = ['title']

admin.site.register(Article, ArticleAdmin)


class MoodAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'text',
    ]

    list_display_links = ['text']

admin.site.register(Mood, MoodAdmin)
