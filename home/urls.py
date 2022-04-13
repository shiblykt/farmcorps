from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('store',views.store,name='store'),
    path('productview',views.productview,name='productview'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('checkout',views.checkout,name='checkout'),
    path('address',views.address,name='address'),
    path('account',views.account,name='account'),
    path('address default',views.defaultAddress,name='defaultAddress'),


]