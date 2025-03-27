from .models import Product, Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog:home_data')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_data.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog:home_data')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:home_data')


class ContactsView(CreateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:home_data')
