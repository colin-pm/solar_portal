from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return render(request, '../templates/index.html')
    else:
        return redirect('portal:login')


def weather(request):
    if request.user.is_authenticated:
        return render(request, '../templates/weather.html')
    else:
        return redirect('portal:login')


def watering(request):
    if request.user.is_authenticated:
        return render(request, '../templates/watering.html')
    else:
        return redirect('portal:login')


def logout_view(request):
    logout(request)
    return redirect('portal:login')
