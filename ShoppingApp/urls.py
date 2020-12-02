from django.urls import path
from ShoppingApp import views
urlpatterns = [
    path('ShoppingCart/',views.ShoppingCart,name = 'ShoppingCart'),
    path('Inventory/',views.Inventory,name = 'Inventory'),
    path('addToCart/',views.addToCart,name = 'addToCart'),
    path('Seller/',views.Seller,name = 'Seller'),
    path('deletefromCart/',views.deletefromCart,name = 'deletefromCart'),
    path('viewProduct/',views.viewProduct,name = 'viewProduct'),
    path('',views.Index,name = 'Index'),
    path('register/',views.Register,name = 'Register'),
    path('login/',views.userLogin,name = 'userLogin'),
    path('logout/',views.userLogout,name = 'userLogout')
]
