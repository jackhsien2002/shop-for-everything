from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.views.generic.list import ListView
import re
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .decorators import member_is_owner_of_product
def product_list(request):

    products = Product.objects.all()

    #每頁顯示3個產品
    paginator = Paginator(products, 3)
    
    page_number = request.GET.get('page')

    page_number = 1 if page_number == None else int(page_number)

    current_page = paginator.page(page_number)
    product_list = paginator.get_page(page_number)
    page_array = list(range(1,paginator.num_pages + 1))

    try:
        previous_page_number = current_page.previous_page_number()
    except:
        previous_page_number = current_page.number
    try:
        next_page_number = current_page.next_page_number()
    except:
        next_page_number = current_page.number

    return render(
        request, 
        'products/list.html', 
        {
            'current_page' : current_page,
            'page_array': page_array,
            'previous_page_number': previous_page_number,
            'next_page_number': next_page_number
        }
    )


def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    return render(request, 'products/detail.html', {'product' : product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(product.get_absolute_url())
    else:
        form = ProductForm(initial={'author':request.user})
    return render(request, 'products/create.html', {'form' : form})

@member_is_owner_of_product
@login_required
@require_http_methods(['POST'])
def product_delete(request):
    product_id = int(request.POST['product_id'])
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('product_delete_success'))


@login_required
def product_delete_success(request):
    return render(request, 'products/product_delete_success.html')

def product_search(request):
    
    if request.method != "GET":
        raise Http404('你沒有權限')
    data=request.GET.get('query', None)
    if data == None:
        data = request.session['query']
    else:
        request.session['query'] = data
    query_list = re.split("[,\- @!~#$%^&*()><?/|]", data)
    query_result = []
    for query_string in query_list:
        query_result.extend(Product.objects.filter(name__icontains=query_string))
    #每頁顯示3個產品
    paginator = Paginator(query_result, 3)
    
    page_number = request.GET.get('page')

    page_number = 1 if page_number == None else int(page_number)

    current_page = paginator.page(page_number)
    product_list = paginator.get_page(page_number)
    page_array = list(range(1,paginator.num_pages + 1))

    try:
        previous_page_number = current_page.previous_page_number()
    except:
        previous_page_number = current_page.number
    try:
        next_page_number = current_page.next_page_number()
    except:
        next_page_number = current_page.number

    return render(
        request, 
        'products/list.html', 
        {
            'current_page' : current_page,
            'page_array': page_array,
            'previous_page_number': previous_page_number,
            'next_page_number': next_page_number
        }
    )