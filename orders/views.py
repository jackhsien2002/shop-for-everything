from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderProduct
from .tasks import send_order_success_email
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your views here.
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
            order_product.save()
        #將訂購清單送到使用者信箱
        
        send_order_success_email.delay(request.user.id, order.id)

        cart.clear()

    return render(request, 'orders/success.html')

def order_list(request):
    user = request.user
    orders = user.orders.all()
    return render(request,'orders/list.html', {'orders':orders})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    print(order)
    products = order.products.all()
    print(products)
    for product in products:
        print(product.product.name)
    return render(request, 'orders/detail.html', {"products": products})

def test_send_order_success_email(user_id, order_id):
    order = Order.objects.get(pk=order_id)
    user = User.objects.get(pk=user_id)
    recipient_list = (
        user.email,
    )

    html_message= render_to_string(
        'orders/email_template.html', 
        {
            'order':order, 
            'user':user
        }
    )

    send_mail(
        subject ='[下單成功]你已經成功下單',
        message = '',
        from_email = 'shopEveryThing@myshop.com',
        recipient_list=recipient_list,
        fail_silently = False,
        html_message=html_message,
    )  

