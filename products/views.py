from django.shortcuts import render
from .models import Product
from .forms import ProductForm
def product_list(request):
    products = Product.objects.all()
    print('this is me')
    print(products)
    return render(request, 'products/list.html', {'products' : products})

def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    return render(request, 'products/detail.html', {'product' : product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return render(request, 'products/detail.html', {'product' : product})
    else:
        form = ProductForm()
    return render(request, 'products/create.html', {'form' : form})

