from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.fcadminLogin,name='fcadminLogin'),
    path('home',views.fcadminHome,name='fcadminHome'),
    path('allsellers',views.adminViewSeller,name='adminViewSeller'),
    path('verifysellers',views.adminVerifySeller,name='adminVerifySeller'),
    path('suspendedsellers',views.adminSuspendedSeller,name='adminSuspendedSeller'),
]