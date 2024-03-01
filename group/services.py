from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils import timezone

from group.models import Group_students
from product.models import Product

User = get_user_model()


def add_student_to_group(user_pk: int, product_pk: int):
    student = User.objects.get(pk=user_pk)
    product = Product.objects.get(pk=product_pk)
    group = (
        Group_students.objects.filter(product=product)
        .annotate(num_students=Count('members'))
        .order_by('num_students')
    ).first()

    if group and group.members.count() < product.max_members:
        group.members.add(student)
        group.save()
    else:
        number = Group_students.objects.filter(product=product).count() + 1
        name_group = 'group_' + str(product.name) + '_' + str(number)
        new_group = Group_students(name=name_group, product=product)
        new_group.save()
        new_group.members.add(student)
        new_group.save()

        group_count = Group_students.objects.filter(product=product).count()
        students_count = product.students_with_access.count()
        if (
            product.min_members <= students_count // group_count <= product.max_members
            and product.started > timezone.now()
        ):
            change_groups(product=product)


def change_groups(product: Product):
    groups = Group_students.objects.filter(product=product).all()
    students = product.students_with_access.all()
    for group in groups:
        group.members.clear()
    for i in range(students.count()):
        group = groups[i % groups.count()]
        group.members.add(students[i])
        group.save()
