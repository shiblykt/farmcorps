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

def adminEditSellerPage(request):
    return render(request,'adm/admin_edit_sellerpage.html')

def adminViewLogistics(request):
    return render(request,'adm/admin_view_logistics.html')

def adminVerifyLogistics(request):
    return render(request,'adm/admin_verify_logistics.html')

def adminSuspendedLogistics(request):
    return render(request,'adm/admin_suspended_logistics.html')

def adminEditLoisticsPage(request):
    return render(request,'adm/admin_edit_logisticspage.html')

def adminEditHomePage(request):
    return render(request,'adm/admin_edit_homepage.html')

def adminChangeCredentials(request):
    return render(request,'adm/admin_change_credentials.html')
