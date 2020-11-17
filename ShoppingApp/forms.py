from django import forms

CATEGORY = (
    ('E', 'Electronics'),
    ('HS', 'HomeSupplies'),
    ('B', 'Books')
)

class SellerForm(forms.Form):
    produtId =forms.IntegerField()
    productName = forms.CharField()
    productPrice = forms.IntegerField()
    productDescription = forms.CharField()
    productSellerName = forms.CharField()
    productColor = forms.CharField()
    ProductCategory = forms.CharField()
    productImage = forms.ImageField()
