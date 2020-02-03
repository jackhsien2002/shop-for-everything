from django.core.exceptions import PermissionDenied
from products.models import Product

def stock_should_enough(view_function):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            quantity = int(request.POST['quantity'])
            product_id = int(request.POST['product_id'])
            product = Product.objects.get(pk=product_id)
            stock = product.stock
            print(quantity, product_id, stock)
            if quantity > stock:
                raise PermissionDenied('庫存不夠')
        return view_function(request, *args, **kwargs)
    return wrapper