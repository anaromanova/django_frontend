from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_mail(
                'Добро пожаловать!',
                'Спасибо за регистрацию!',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('catalog:home_data')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalog:home_data')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
