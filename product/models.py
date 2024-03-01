from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=100)
    started = models.DateTimeField(verbose_name='Дата и время старта продукта')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор продукта',
        related_name='products',
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена продукта'
    )
    min_members = models.IntegerField(
        default=0, verbose_name='Минимальное количество участников'
    )
    max_members = models.IntegerField(
        default=5, verbose_name='Максимальное количество участников'
    )

    students_with_access = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = [
            'name',
        ]

    def __str__(self) -> str:
        return f'{self.name}'
