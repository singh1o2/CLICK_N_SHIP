from django.shortcuts import render
from ShoppingApp.models import Product,Cart,product,index
from ShoppingApp.forms import SellerForm
from ShoppingApp import models
from django.http import HttpResponse
import json,os
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
    if request.method == 'POST':
        form = SellerForm(request.POST,request.FILES)
        print(form.is_valid())
        print(form.errors)
        if(form.is_valid()):
            form.save()
            return HttpResponse("FORM SUBMITED!!")
        return HttpResponse("INVALID FORM")
    else:
        form  = SellerForm()
        return render(request,'Seller.html',{'form': form})

def viewProduct(request):
    if request.method == 'POST':
        models.index+=1;
        productName =json.loads(request.body)
        productList  = Product.objects.all()
        for r in productList:
            if(r.productName==productName):
                item = r
        models.product.append(item)
        return HttpResponse("Hi")

    else:
        return render(request,'viewProduct.html',{'item': models.product[models.index]})



def addToCart(request):
    productName =json.loads(request.body)
    productList  = Product.objects.all()
    for r in productList:
        if(r.productName==productName):
            item = r
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
