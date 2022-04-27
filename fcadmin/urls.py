from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.fcadminLogin,name='fcadminLogin'),
    path('home',views.fcadminHome,name='fcadminHome'),
    path('allsellers',views.adminViewSeller,name='adminViewSeller'),
    path('verifysellers',views.adminVerifySeller,name='adminVerifySeller'),
    path('suspendedsellers',views.adminSuspendedSeller,name='adminSuspendedSeller'),
    path('editseller',views.adminEditSellerPage,name='adminEditSellerPage'),

    path('alllogistics',views.adminViewLogistics,name='adminViewLogistics'),
    path('verifylogistics',views.adminVerifyLogistics,name='adminVerifyLogistics'),
    path('suspendedlogistics',views.adminSuspendedLogistics,name='adminSuspendedLogistics'),
    path('editlogistics',views.adminEditLoisticsPage,name='adminEditLoisticsPage'),
    path('editcustomerhome',views.adminEditHomePage,name='adminEditHomePage'),
    path('accountinfo',views.adminChangeCredentials,name='adminChangeCredentials'),
]