from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.detail,name = 'detail'),
    path('searchData/',views.searchData,name = 'searchData')
]