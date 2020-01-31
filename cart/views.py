from django.shortcuts import render
from .cart import Cart
def cart_update(request):
    if request.method == "POST":
        product_id = int(request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        cart = Cart(request)
        product = Product.objects.get(pk=product_id)
        update_quantity = True if cart.is_product_exist(product_id) else False
        cart.add(product, quantity, update_quantity)
        print(f"price {cart.get_total_price()}")
        print(f"quantity {len(cart)}")
    return redirect(product.get_absolute_url())

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart' : cart})