from django.contrib import admin

from group.models import Group_students


@admin.register(Group_students)
class ProductAdmin(admin.ModelAdmin):
    """Админ панель модели Группа"""

    list_display = 'id', 'name', 'product'
    list_display_links = ('name',)
    search_fields = ('name',)
