from django import forms
from ShoppingApp.models import Product,User
from django.contrib.auth.models import User

class SellerForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['produtId','productName','productPrice','productDescription','productColor','productSellerName','productImage','ProductCategory',]
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','email','password']
