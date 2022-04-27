from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'customer/customer_home.html')

def customerSignup(request):
    return render(request,'customer/customer_signup.html')

def signin(request):
    return render(request,'customer/customer_signin.html')

def forgotpassword(request):
    return render(request,'customer/forgot_password.html')

def store(request):
    return render(request,'customer/store.html')

def productview(request):
    return render(request,'customer/product_view.html')

def wishlist(request):
    return render(request,'customer/customer_wishlist.html')

def checkout(request):
    return render(request,'customer/customer_checkout.html')

def address(request):
    return render(request,'customer/customer_address.html')

def account(request):
    return render(request,'customer/customer_account.html')

def defaultAddress(request):
    return render(request,'customer/customer_default_address.html')