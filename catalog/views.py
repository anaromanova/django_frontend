from tkinter.font import names

from django.http import HttpResponse
from django.shortcuts import render


def home_data(request):
    if request.method == "GET":
        return render(request, "catalog/home.html")


def contacts_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Данные отправлены, {name}")
    return render(request, "catalog/contacts.html")
