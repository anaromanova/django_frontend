from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def home_data(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "catalog/home.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, "catalog/product_details.html", context)


def contacts_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Данные отправлены, {name}")
    return render(request, "catalog/contacts.html")


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home_data')  # Перенаправление на список товаров
    else:
        form = ProductForm()

    return render(request, 'catalog/add_products.html', {'form': form})