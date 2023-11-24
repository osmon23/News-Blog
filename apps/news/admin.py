from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'date',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'id',
        'title',
        'author',
        'date',
    )
    list_filter = (
        'id',
        'title',
        'author',
        'date',
    )
