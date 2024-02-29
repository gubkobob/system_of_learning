from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User
from django.db import models

from product.models import Product

User = get_user_model()


class Group_students(models.Model):
    """Модель группы"""

    name = models.CharField(max_length=100)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="К какому продукту относится группа",
        related_name="groups",
    )
    members = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return f"{self.name}"
