from django.contrib import admin

from lesson.models import Lesson


@admin.register(Lesson)
class ProductAdmin(admin.ModelAdmin):
    """Админ панель модели Урок"""

    list_display = "id", "video_link", "name", "product"
    list_display_links = ("name",)
    search_fields = ("name",)
