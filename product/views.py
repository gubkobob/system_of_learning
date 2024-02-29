from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from group.services import add_student_to_group
from product.models import Product

User = get_user_model()


class ProductsListView(ListView):
    template_name = 'products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.select_related('author').annotate(
        num_lessons=Count('lessons')
    )


def add_user_to_product(
    request: HttpRequest, user_pk: int, product_pk: int
) -> HttpResponse:
    student = User.objects.get(pk=user_pk)
    product = Product.objects.get(pk=product_pk)
    if student not in product.students_with_access.all():
        product.students_with_access.add(student)
        product.save()
        add_student_to_group(user_pk=user_pk, product_pk=product_pk)
        return HttpResponse(f'User {student} added to product {product}')
    else:
        return HttpResponse(f'User {student} already have access to product {product}')
