from .models import Product
from django.forms import ModelForm, HiddenInput
from django.utils.translation import gettext_lazy as _

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['author', 'name', 'description', 'price', 'stock', 'image']
        widgets = {'author':HiddenInput()}
        labels = {
            'author': _('店家'),
            'name': _('商品名稱'),
            'description': _('商品描述'),
            'price': _('價位'),
            'stock': _('庫存'),
            'image': _('商品圖片'),
        }