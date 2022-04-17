from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.landing,name='landing'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('bankInfo',views.bankInfo,name='bankInfo'),
    path('buisnessInfo',views.buisnessInfo,name='buisnessInfo'),
]