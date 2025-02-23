from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home_data/", views.home_data, name="home_data"),
    path("contacts_data/", views.contacts_data, name="contacts_data"),
]
