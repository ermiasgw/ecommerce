

from django.test import Client,TestCase
from store.models import Catagory, Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestBasketView(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='admin')
        Catagory.objects.create(name='django', slug='django')
        Product.objects.create(catagory_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00')
        Product.objects.create(catagory_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00')
        Product.objects.create(catagory_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00')
        
        self.client.post(
            reverse('basket:basket_add'),{"productid": 1, "productqty": 1, "action":"post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'),{"productid": 2, "productqty": 2, "action":"post"}, xhr=True)

    def test_basket_url(self):
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        response = self.client.post(reverse('basket:basket_add'),{"productid": 3, "productqty": 1, "action":"post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        
        response = self.client.post(reverse('basket:basket_add'),{"productid": 2, "productqty": 1, "action":"post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 5})

    def test_basket_delete(self):
        response = self.client.post(
            reverse('basket:basket_delete'),{ "productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': "20.00"})

    def test_basket_update(self):
        response = self.client.post(reverse('basket:basket_update'),{"productid": 2, "productqty": 1, "action":"post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})


    
