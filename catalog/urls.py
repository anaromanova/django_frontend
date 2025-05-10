from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

app_name = "catalog"

urlpatterns = [
    path('home_data/', views.ProductListView.as_view(), name="home_data"),
    path('contacts_data/', views.ContactsView.as_view(), name="contacts"),
    path('product_details/<int:pk>/', views.ProductDetailView.as_view(), name="product_details"),
    path('add_products/', views.ProductCreateView.as_view(), name="add_products"),
    path('post/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update_product'),
    path('post/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('post/<int:pk>/unpublish/', views.unpublish_product, name='unpublish_product'),
    path('category/<int:category_id>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
