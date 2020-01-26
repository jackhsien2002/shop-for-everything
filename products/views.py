from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    print('this is me')
    print(products)
    return render(request, 'products/list.html', {'products' : products})

def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    return render(request, 'products/detail.html', {'product':product})
