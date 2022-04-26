from django.shortcuts import render

def fcadminLogin(request):
    return render(request,'adm/admin_login.html')

def fcadminHome(request):
    return render(request,'adm/admin_home.html')

def adminViewSeller(request):
    return render(request,'adm/admin_view_seller.html')

def adminVerifySeller(request):
    return render(request,'adm/admin_verify_seller.html')

def adminSuspendedSeller(request):
    return render(request,'adm/admin_suspended_sellers.html')
