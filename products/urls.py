from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:slug>', views.product_detail, name = 'detail'),
    path('list', views.product_list, name = "list"),
]
