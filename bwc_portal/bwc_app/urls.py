from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),
    path('readers/', views.readers_tab, name='readers_tab'),
    path('shopping', views.shopping, name='shopping'),
    path('save', views.save, name='save'),
    path('readers/add', views.save_reader, name='save_reader'),
]
