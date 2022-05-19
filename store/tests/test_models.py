from django.test import TestCase
from store.models import Catagory, Product

class Test_mmodels(TestCase):
    def setUp(self):
        self.data1 = Catagory.objects.create(name='django', slug='django')
        
    def test_catagory_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data,Catagory))
    def test_catagory_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'django1')
