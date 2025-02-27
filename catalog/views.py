from .models import Product, Contact
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'price', 'description', 'category', 'image']
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog/home_data')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_data.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class ContactsView(CreateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:home_data')
