from django.urls import path
from . import views

urlpatterns = [
    path('FPS/',views.dashboard,name = 'dashboard'),
    path('sell/',views.sell,name = 'sell'),
    path('requests/',views.Requests,name = 'Requests'),
    path('customers/',views.customers,name = 'customers'),
    path('ration/<int:pk>/',views.update_status,name = 'update_status'),
    path('search/',views.check_user,name = 'check_user')
]