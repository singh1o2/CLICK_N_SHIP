from django.test import SimpleTestCase
from django.urls import reverse,resolve
from ShoppingApp.views import Index, Inventory, addToCart,deletefromCart,viewProduct,Seller,ShoppingCart

#This is for testing url links
class TestUrls(SimpleTestCase):
    def test_indexUrl(self):
        url = reverse('Index')
        self.assertEquals(resolve(url).func,Index)
        print("....Index URL tested...Ok\n")

    def test_inventoryUrl(self):
        url = reverse('Inventory')
        self.assertEquals(resolve(url).func,Inventory)
        print("....Inventory URL tested...Ok\n")

    def test_addToCartUrl(self):
        url = reverse('addToCart')
        self.assertEquals(resolve(url).func,addToCart)
        print("....addToCart URL tested...Ok\n")

    def test_deletefromCartUrl(self):
        url = reverse('deletefromCart')
        self.assertEquals(resolve(url).func,deletefromCart)
        print("....deletefromCart URL tested...Ok\n")

    def test_viewProductUrl(self):
        url = reverse('viewProduct')
        self.assertEquals(resolve(url).func,viewProduct)
        print("....viewProduct URL tested...Ok\n")

    def test_SellerUrl(self):
        url = reverse('Seller')
        self.assertEquals(resolve(url).func,Seller)
        print("....Seller URL tested...Ok\n")

    def test_ShoppingCartUrl(self):
        url = reverse('ShoppingCart')
        self.assertEquals(resolve(url).func,ShoppingCart)
        print("....ShoppingCart URL tested...Ok\n")
