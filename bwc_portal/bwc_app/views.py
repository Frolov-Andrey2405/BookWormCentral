from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', context={"current_tab": "home"})


def readers(request):
    return render(request, 'readers.html', context={"current_tab": "readers"})


def shopping(request):
    return HttpResponse("Welcome to Shopping")


def save(request):
    name = request.POST['name']
    return render(request, 'welcome.html', context={'name': name})
