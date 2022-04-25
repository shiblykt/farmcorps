from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'reseller/reseller_landing.html')

def sellerLogin(request):
    return render(request,'reseller/reseller_login.html')

def registration(request):
    return render(request,'reseller/reseller_registration.html')

def bankInfo(request):
    return render(request,'reseller/reseller_bankdetails.html')

def buisnessInfo(request):
    return render(request,'reseller/reseller_buisnessInfo.html')

def home(request):
    return render(request,'reseller/reseller_home.html')

def addVeg(request):
    return render(request,'reseller/add_veggies.html')

def editVeg(request):
    return render(request,'reseller/edit_veggies.html')

def newOrders(request):
    return render(request,'reseller/reseller_manage_order.html')

def shipment(request):
    return render(request,'reseller/shipment_mode.html')

