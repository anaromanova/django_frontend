from django.contrib import admin
from catalog.models import Product, Category, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    search_fields = ("category_name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "price", "category")
    list_filter = ("category",)
    search_fields = ("product_name", "description")

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "message")
    list_filter = ("name",)
    search_fields = ("name", "phone")
