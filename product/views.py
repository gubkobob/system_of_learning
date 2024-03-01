from django.contrib.auth import get_user_model
from django.db.models import Count, OuterRef, Subquery
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from group.services import add_student_to_group
from product.models import Product

User = get_user_model()


class ProductsListView(ListView):
    template_name = 'products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.annotate(num_lessons=Count('lessons'))


class ProductsStatisticListView(ListView):
    template_name = 'products-list_statistic.html'
    context_object_name = 'products'

    queryset = Product.objects.annotate(
        num_students_with_access=Subquery(
            Product.objects.filter(pk=OuterRef('pk'))
            .annotate(num_st=Count('students_with_access'))
            .values('num_st')[:1]
        ),
        num_groups=Subquery(
            Product.objects.filter(pk=OuterRef('pk'))
            .annotate(num_gr=Count('groups'))
            .values('num_gr')[:1]
        ),
        num_students=Count('groups__members'),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_all_users = User.objects.count()

        for product in context['products']:
            product.pers_purchase = round(
                product.num_students_with_access / num_all_users * 100
            )
            if product.num_groups:
                product.avg_filled = round(
                    product.num_students
                    / product.max_members
                    / product.num_groups
                    * 100
                )
            else:
                product.avg_filled = 0
        return context


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
