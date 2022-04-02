from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'customer_signup.html')

def signin(request):
    return render(request,'customer_signin.html')

def forgotpassword(request):
    return render(request,'forgot_password.html')