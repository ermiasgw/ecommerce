from encodings import utf_8
from unittest import skip
from urllib import request, response
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Catagory, Product
from django.test import Client
from django.urls import reverse
from django.http import HttpRequest
from store.views import all_products
class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        """
        def test_product(self):
                response = self.c.get(reverse('store:product_detail', args=['django']))
                self.assertEqual(response.status_code, 200)
        """
    
    def test_homehtml(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)

