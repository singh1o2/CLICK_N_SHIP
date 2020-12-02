from django.shortcuts import render
from ShoppingApp.models import Product,Cart,product,index,User
from ShoppingApp.forms import SellerForm,UserForm
from ShoppingApp import models
from django.http import HttpResponse,HttpResponseRedirect
import json,os

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
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

def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()

    return render(request,'Register.html',{'user_form':user_form,'registered':registered})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Index'))
            else:
                return HttpResponse('user not active ...')
        else:
            return render(request,'Login.html')

    else:
        return render(request,'Login.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('..')

def addToCart(request):
    productName= json.loads(request.body)
    productList  = Product.objects.all()
    for r in productList:
        if(r.productName==productName):
            item = r
            Cart.objects.create(product=item, productQuantity=1)
    return HttpResponse("Item added to Car")


def deletefromCart(request):
    productName = json.loads(request.body)
    productList  = Cart.objects.all()
    for r in productList:
        if(r.product.productName==productName):
            item = r.product
    Cart.objects.filter(product=item).delete()
    return HttpResponse("hi")
