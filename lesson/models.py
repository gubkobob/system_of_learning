from django.db import models

from product.models import Product


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(max_length=100)
    video_link = models.TextField(blank=True, verbose_name="ссылка на видео")

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="К какому продукту относится урок",
        related_name="lessons",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return f"{self.name}"
