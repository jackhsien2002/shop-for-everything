from .models import Product
from django.forms import ModelForm, HiddenInput

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['author', 'name', 'description', 'price', 'stock', 'image']
        widgets = {'author':HiddenInput()}