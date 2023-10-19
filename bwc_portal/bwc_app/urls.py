from django.contrib import admin
from django.urls import path
from .views import home, shopping, save

urlpatterns = [
    path('home', home),
    path('shopping', shopping),
    path('save', save),
]
