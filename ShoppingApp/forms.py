from django import forms
from ShoppingApp.models import Product


class SellerForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['produtId','productName','productPrice','productDescription','productColor','productSellerName','productImage','ProductCategory',]
