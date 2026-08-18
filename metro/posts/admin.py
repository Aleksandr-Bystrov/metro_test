from django.contrib import admin

from .models import Post

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    """Класс для настройки админ-зоны."""

    list_display = (
        'content',
        'created_at',
        'updated_at',
        'author',
        'image',
    )
    search_fields = (
        'content',
    )
    list_filter = (
        'author',
    )


admin.site.register(Post, PostAdmin)
