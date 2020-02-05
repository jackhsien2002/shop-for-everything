from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderProduct
from .tasks import send_order_success_email
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.decorators import stock_should_enough
# Create your views here.
@login_required
def checkout(request):
    if request.method == 'POST':
        order = Order(customer=request.user)
        order.save()
        cart = Cart(request)
        for item in cart:
            product = item['product']
            order_product = OrderProduct(
                order = order,
                from_user = request.user,
                to_user = product.author,
                product = product,
                quantity = item['quantity'],
                expense = item['total_price'],
            )
            product.update_stock(product.stock - item['quantity'])
            product.save()
            order_product.save()
        #將訂購清單送到使用者信箱
        
        send_order_success_email(request.user.id, order.id)

        cart.clear()

    return render(request, 'orders/success.html')

@login_required
def order_list(request):
    user = request.user
    orders = user.orders.all()
    return render(request,'orders/list.html', {'orders':orders})

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    products = order.products.all()
    for product in products:
        print(product.product.name)
    return render(request, 'orders/detail.html', {"products": products})

