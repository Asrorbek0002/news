from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published")
    list_filter = ("is_published", "category")
