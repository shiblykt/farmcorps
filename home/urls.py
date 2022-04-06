from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('store',views.store,name='store'),
]