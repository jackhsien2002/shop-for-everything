from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderProduct
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




