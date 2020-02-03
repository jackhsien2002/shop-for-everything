from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.cart_update, name="update_cart"),
    path('detail/', views.cart_detail, name="cart_detail"),
]