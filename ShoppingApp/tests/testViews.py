from django.test import TestCase,Client
from django.urls import reverse
from ShoppingApp.models import Product,Cart
from ShoppingApp.forms import SellerForm
import json
#This is page for testing the actual content loaded on main page and addToCart functionality when get or post request is made
class TestViews(TestCase):
        def test_indexView(self):
            client = Client()
            response = client.get(reverse('Index'))
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,'Index.html')
            print("....main page tested...template loaded...OK\n")

        def test_SellerView_addToCart(self):
            client = Client()
            response = client.post(reverse('addToCart'),json.dumps({'productName':'Laptop'}),json.dumps({'productName':'Laptop'}))
            self.assertEqual(response.status_code,200)
            print("....addToCart function tested......data Sent to Cart Successfully...OK\n")
