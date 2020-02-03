from django.test import TestCase
from ..models import Product
from django.contrib.auth.models import User
from unidecode import unidecode
from django.utils.text import slugify
# Create your tests here.
class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User(
            username = 'test_user',
            password = 'test_password',
        )
        cls.user.save()

        cls.product = Product(
            name = "測試產品",
            price = 100,
            description = "測試產品描述",
            author = cls.user,
        )
        cls.product.save()

    def test_name_max_length(self):
        #在test裡，被建立的第一個物件id為1
        product = Product.objects.get(pk=1)
        print(product.slug)
        max_length = product._meta.get_field('name').max_length
        #左邊實際值 右邊期望值
        self.assertEquals(max_length, 50)
        
    def test_slug_is_unique(self):
        product = Product.objects.get(pk=1)
        is_unique = product._meta.get_field('slug').unique
        self.assertEquals(is_unique, True)

    def test_slug_not_null(self):
        product = Product.objects.get(pk=1)
        is_null = product._meta.get_field('slug').null
        self.assertEquals(is_null, False)
    
    def test_pubdate_field_label(self):
        product = Product.objects.get(pk=1)
        field_label = product._meta.get_field('pub_date').verbose_name
        self.assertEquals(field_label, 'first published date')
    
    def test_last_date_field_label(self):
        product = Product.objects.get(pk=1)
        field_label = product._meta.get_field('last_date').verbose_name
        self.assertEquals(field_label, 'last modified date')
    
    def test_default_image_path(self):
        product = Product.objects.get(pk=1)
        image = product.image
        self.assertEquals(image.url, '/media/default.jpg')
