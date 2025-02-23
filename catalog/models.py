from tkinter.font import names

from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.CharField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name", "description"]

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Название категории",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(
        blank=True, default=0.0, verbose_name="Цена", help_text="Введите цену продукта"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата изменения",
        help_text="Введите дату изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "description"]

    def __str__(self):
        return self.product_name
