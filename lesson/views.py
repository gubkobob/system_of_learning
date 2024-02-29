from django.shortcuts import render
from django.views.generic import ListView

from lesson.models import Lesson
from product.models import Product


class LessonsListView(ListView):
    template_name = "lessons-list.html"
    context_object_name = "lessons"
    queryset = Lesson.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = Product.objects.get(pk=self.kwargs.get("product_pk"))

        if user in product.students_with_access.all():
            lessons = Lesson.objects.select_related("product").filter(product=product)
        else:
            lessons = []

        context["lessons"] = lessons
        context["product"] = product
        return context
