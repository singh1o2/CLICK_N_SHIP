from django.urls import path
from ShoppingApp import views
urlpatterns = [
    path('ShoppingCart/',views.ShoppingCart,name = 'ShoppingCart'),
    path('Inventory/',views.Inventory,name = 'Inventory'),
    path('',views.Index,name = 'Index')
]
