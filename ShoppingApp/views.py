from django.shortcuts import render
from ShoppingApp.models import Product,Cart
from ShoppingApp.forms import SellerForm
from django.http import HttpResponse
import json
# Create your views here.s
def Index(request): # for main page
    productList  = Product.objects.all()
    dic = {'records' : productList}
    return render(request,'Index.html',context = dic)

def ShoppingCart(request): # for ShoppingCart
    productList  = Cart.objects.all()
    dic = {'records' : productList}
    return render(request,'ShoppingCart.html',context = dic)

def Inventory(request): # for Inventory
    productList  = Product.objects.all()
    dic = {'records' : productList}
    return render(request,'Inventory.html',context = dic)

def Seller(request): # for Seller
    form  = SellerForm()
    print(request.FILES['productImage']);
    if request.method == 'POST':
        form = SellerForm(request.POST)
        print(form.is_valid());
        if(form.is_valid()):
            print(form.cleaned_data['productName'])
            print(form.cleaned_data['productPrice'])
            print(form.cleaned_data['productSellerName'])
    return render(request,'Seller.html',{'form': form})

def addToCart(request):
    productName =json.loads(request.body)
    productList  = Product.objects.all()
    for r in productList:
        if(r.productName==productName):
            item = r
    print(item)
    Cart.objects.create(product=item, productQuantity=1)
    return HttpResponse("hi")


def deletefromCart(request):
    productName = json.loads(request.body)
    productList  = Cart.objects.all()
    for r in productList:
        if(r.product.productName==productName):
            item = r.product
    Cart.objects.filter(product=item).delete()
    return HttpResponse("hi")
