from django.shortcuts import render
# Create your views here.
def Index(request): # for main page
    dic = {'IndexHead' : 'This is Main Page'}
    return render(request,'Index.html',context = dic)

def ShoppingCart(request): # for ShoppingCart
    dic1 = {'ShopHead' : 'This is ShoppingCart'}
    return render(request,'ShoppingCart.html',context = dic1)

def Inventory(request): # for Inventory
    dic2 = {'InventoryHead' : 'This is Inventory'}
    return render(request,'Inventory.html',context = dic2)
