from django.urls import path
from . import views

urlpatterns = [
    path('Govt/',views.send,name = 'send'),
    path('Reports/',views.reports,name = 'reports'),
    path('Orders/',views.orders,name = 'orders'),
    path('People/',views.people,name = 'people'),
    path('Add/',views.add,name = 'add'),
    # path('pdf/<str:pk>',views.getpdf,name = 'pdf'),
    # path('pdf/test/',views.showPdf,name='showPdf'),
    path('report/<str:shop>/<int:month>/<int:year>',views.showPdf,name='showPdf'),
    path('searchReport/',views.searchReport,name = 'searchReport')
]