from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя и Фамилия",
        help_text="Введите ваше имя и фамилию",
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Введите описание категории",
        unique=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="Введите ваше сообщение",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["phone", "name", "message"]

    def __str__(self):
        return self.phone


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
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

    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    ]

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
    price = models.DecimalField(
        blank=True,
        default=0.0,
        verbose_name="Цена",
        help_text="Введите цену продукта",
        decimal_places=2,
        max_digits=100
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения",
        help_text="Введите дату изменения",
        default = timezone.now
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец',
        null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "description"]
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]

    def __str__(self):
        return self.product_name
