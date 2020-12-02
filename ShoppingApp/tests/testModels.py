from django.test import TestCase
from ShoppingApp.models import Product,Cart

#This page is for testing the models created for database interaction
class TestModels(TestCase):

    def test_productModel(self):
        p = Product.objects.create(
        produtId= 1255,
        productName= 'Speaker',
        productPrice=53.5,
        productDescription='This is Speaker',
        productColor='Red',
        productSellerName='Google',
        productImage='speaker.jpg',
        )
        for p in Product.objects.all(): #accessing all products in database
            if p.produtId == 1255:
                self.assertTrue(p.productPrice,'53.5')
        print("....productModel passed the test...\n")

    def test_CartModel(self):
        p = Product.objects.create(
        produtId= 12557,
        productName= 'Homepod',
        productPrice=53.5,
        productDescription='This is Speaker',
        productColor='Grey',
        productSellerName='Apple',
        productImage='Homepod.jpg',
        )
        cart = Cart.objects.create(
            product = p,
            productQuantity = 12
            )
        for p in Cart.objects.all(): #accessing all products in cart in database
            if p.product.produtId == 12557:
                self.assertTrue(p.productQuantity,'12')
        print("....CartModel passed the test...\n")
