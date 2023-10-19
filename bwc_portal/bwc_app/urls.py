from django.contrib import admin
from django.urls import path
from .views import home, readers, shopping, save

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers', readers),
    path('shopping', shopping),
    path('save', save),
]
