from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('detail', views.product_detail, name = 'detail'),
]