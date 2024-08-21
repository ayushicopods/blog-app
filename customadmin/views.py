from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=email)
        if not user.exists():
            user = User.objects.create_superuser(username=email, password=password)
        user = authenticate(request, username=email, password=password)
        if user and user.is_superuser:
            login(request, user)
            return redirect('/products/')
    return render(request, 'customAdmin.html')