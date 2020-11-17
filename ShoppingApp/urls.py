from django.urls import path
from ShoppingApp import views
urlpatterns = [
    path('ShoppingCart/',views.ShoppingCart,name = 'ShoppingCart'),
    path('Inventory/',views.Inventory,name = 'Inventory'),
    path('addToCart/',views.addToCart,name = 'addToCart'),
    path('Seller/',views.Seller,name = 'Seller'),
    path('deletefromCart/',views.deletefromCart,name = 'deletefromCart'),
    path('',views.Index,name = 'Index')
]
