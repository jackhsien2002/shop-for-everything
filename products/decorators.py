from .models import Product
from django.core.exceptions import PermissionDenied
def member_is_owner_of_product(view_function):
    def wrapper(request, *args, **kwargs):
        product_id = int(request.POST['product_id'])
        product = Product.objects.get(pk = product_id)
        owner_id = product.author.id
        member_id = request.user.id
        if owner_id == member_id:
            return view_function(request, *args, **kwargs)
        else:
            raise PermissionDenied("你沒有權限刪除該商品")
    return wrapper