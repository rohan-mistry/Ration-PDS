from django.shortcuts import render
import requests
from accounts.decorators import customer_required
from datetime import date
from FPS.models import SoldRation
from Govt.models import CustomerRegistration
from .forms import SearchForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.

@customer_required
def detail(request):
    today = date.today()
    dataSearch = {}
    ration_id = request.user.customer.ration_id
    try:
        info = CustomerRegistration.objects.get(rationid = ration_id)
    except CustomerRegistration.DoesNotExist:
        info = None
    try:
        generalData = SoldRation.objects.get(rationid = ration_id,date_month = today.month,date_year = today.year)
    except SoldRation.DoesNotExist:
        generalData = None
    print('info : ')
    print(info)  
    return render(request,'Customer/detail.html',{'generalData':generalData,'info':info,'dataSearch':dataSearch})


def searchData(request):
    if request.method=='POST':
        data = request.POST
        month = data.get('month')
        year = data.get('year')
        ration_id = data.get('rationid')
        print(month)
        print(year)
        try:
            dataSearch = SoldRation.objects.get(rationid = ration_id,date_month = month,date_year = year)
        except SoldRation.DoesNotExist:
            dataSearch = None
        if dataSearch:
            return JsonResponse({'found':1,'dataSearch':model_to_dict(dataSearch)},status = 200)

    return JsonResponse({'found':0},status = 200)    