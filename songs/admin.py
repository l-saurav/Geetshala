from django.contrib import admin

from .models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('title', 'lyrics', 'release_date', 'is_published')
    list_display = ('title', 'release_date', 'is_published')
    search_fields = ('title', 'lyrics')
    list_filter = ('is_published', 'release_date')
    ordering = ('-release_date', 'title')
