from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (
    ('E', 'Electronics'),
    ('HS', 'HomeSupplies'),
    ('B', 'Books')
)

product = []
index = -1

class Product(models.Model):
    produtId =models.IntegerField(unique=True)
    productName = models.CharField(max_length = 50)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productSellerName = models.CharField(max_length = 50)
    productColor = models.CharField(max_length = 50)
    ProductCategory = models.CharField(choices=CATEGORY, max_length=2)
    productImage = models.ImageField(upload_to='images/')

class Cart(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    productQuantity = models.IntegerField()

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
