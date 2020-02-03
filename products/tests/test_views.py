from django.test import TestCase
from django.urls import reverse
class ProductListViewTest(TestCase):

    def test_url_exist_at_address(self):
        response = self.client.get('/product/list')
        self.assertEquals(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('product_list'))
        print(reverse('product_list'))
        self.assertEquals(response.status_code,200)
    
    def test_view_use_correct_template(self):
        response = self.client.get('/product/list')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/list.html')