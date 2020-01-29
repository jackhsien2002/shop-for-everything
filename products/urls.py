from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:slug>', views.product_detail, name = 'product_detail'),
    path('list', views.product_list, name = "product_list"),
    path('create', views.product_create, name='product_create'),
]
