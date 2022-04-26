from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.logisticsLanding,name='logisticsLanding'),
    path('login',views.logisticsLogin,name='logisticsLogin'),
    path('signup',views.signup,name='signup'),
    path('bank-details',views.bankDetails,name='bankDetails'),
    path('buisnessInfo',views.buisnessDetails,name='buisnessDetails'),
    path('home',views.home,name='logisticsHome'),
    path('manageRequests',views.manageRequests,name='manageRequests'),
]