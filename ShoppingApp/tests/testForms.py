from  django.test import TestCase
from ShoppingApp.forms import SellerForm

#This is for testing if the seller from used for taking product info from seller 
class TestForms(TestCase):
     def test_SellerForm(self):
         form = SellerForm(data={
            'produtId':1230,
            'productName': 'Speaker',
            'productPrice':53,
            'productDescription':'This is Speaker',
            'productColor':'Red',
            'productSellerName':'Google',
            'ProductCategory':'E'
            })
         self.assertTrue(form.is_valid())
         print("....Seller Form tested...Ok\n")
