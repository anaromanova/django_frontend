from .models import Product, Contact, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.cache import cache
from catalog.services import get_products_by_category


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog:home_data')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_data.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        cache_key = f'product_detail_{pk}'
        product = cache.get(cache_key)

        if product is None:
            product = super().get_object(queryset)
            cache.set(cache_key, product, timeout=60 * 5)  # 5 минут

        return product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog:home_data')

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:home_data')

    @method_decorator(permission_required('products.delete_product', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Проверяем, что пользователь либо владелец, либо имеет право на удаление
        if product.owner != request.user and not request.user.has_perm('products.delete_product'):
            raise PermissionDenied("Вы не можете удалить этот продукт.")

        return super().dispatch(request, *args, **kwargs)


class ProductsByCategoryView(ListView):
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return get_products_by_category(category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs.get('category_id'))
        return context


class ContactsView(CreateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:home_data')


@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.status = 'draft'
        product.save()
        return redirect('catalog:home_data')
    return render(request, 'catalog/unpublish_product.html', {'product': product})


