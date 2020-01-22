from django.shortcuts import render

def product_detail(request):
    return render(request, 'products/detail.html')
