from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('<int:list_id>', views.delete, name='delete'),
]
