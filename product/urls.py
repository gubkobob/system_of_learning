from django.urls import path

from product.views import ProductsListView, add_user_to_product

app_name = 'product'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path(
        '<int:product_pk>/add_student/<int:user_pk>',
        add_user_to_product,
        name='add_user_to_product',
    ),
]
