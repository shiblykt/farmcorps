from django.shortcuts import render

def logisticsLanding(request):
    return render(request,'logistic/logistics_landing.html')

def logisticsLogin(request):
    return render(request,'logistic/logistics_login.html')

def signup(request):
    return render(request,'logistic/logistics_signup.html')

def bankDetails(request):
    return render(request,'logistic/logistics_bankinfo.html')

def buisnessDetails(request):
    return render(request,'logistic/logistics_buisnessInfo.html')

def home(request):
    return render(request,'logistic/logistics_home.html')

def manageRequests(request):
    return render(request,'logistic/manage_requests.html')