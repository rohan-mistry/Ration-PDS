from django.urls import path,include
from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.home, name='home'),
    path('accounts/signup/FPS/', views.FPSSignUpView.as_view(), name='FPS_signup'),
    path('accounts/signup/Customer/', views.CustomerSignUpView.as_view(), name='Customer_signup'),
    path('',views.home,name ='home'),
  

]