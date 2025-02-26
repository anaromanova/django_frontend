from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

app_name = "catalog"

urlpatterns = [
    path('home_data/', views.home_data, name="home_data"),
    path('contacts_data/', views.contacts_data, name="contacts_data"),
    path('product_details/<int:product_id>/', views.product_details, name="product_details"),
    path('add_products/', views.add_products, name="add_products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
