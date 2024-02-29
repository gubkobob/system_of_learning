from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ панель модели Продукт"""

    list_display = (
        'id',
        'started',
        'name',
        'author',
        'price',
        'min_members',
        'max_members',
    )
    list_display_links = ('name',)
    search_fields = ('name',)
