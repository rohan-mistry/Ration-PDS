from django.shortcuts import render,redirect
import requests
from accounts.decorators import FPS_required
from django.contrib.auth.decorators import login_required
from .models import SoldRation,Stock,Reports,FPSRequest
from .forms import Sold 
from Govt.models import CustomerRegistration,RationSent
from django.http import JsonResponse
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

@FPS_required
def dashboard(request):
    incoming = RationSent.objects.filter(shopid = request.user.shop.shopid).order_by('-date')
    try:
        stock = Stock.objects.get(shop = request.user.shop)
    except Stock.DoesNotExist:
        stock = None
    page_obj = paginationObject(request,incoming,5)
    print(incoming)
    context = {'incoming' : page_obj,'stock':stock}
    return render(request,'FPS/dashboard.html',context)

@FPS_required
def sell(request):
    sales = SoldRation.objects.filter(shop=request.user.shop).order_by('-date')
    today = date.today()
    if request.method=='POST':
        form = Sold(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                customer = CustomerRegistration.objects.get(shopid = request.user.shop.shopid,rationid =data['rationid'] )
                customer_ration = SoldRation.objects.get( date_month = today.month,date_year = today.year, rationid = data['rationid'])
            except CustomerRegistration.DoesNotExist:
                customer = None
            except SoldRation.DoesNotExist:
                customer_ration = None
            if Stock.objects.filter(shop=request.user.shop).count()==0:
                messages.info(request, 'Currently no stocks are available !')
                return redirect('sell')
            elif not(customer):
                messages.info(request, 'Customer is not registered!')    
                return redirect('sell')    
            elif customer_ration :
                messages.info(request, 'Quota for this month is over!')    
                return redirect('sell')
            else:
                stock = Stock.objects.get(shop=request.user.shop)
                if(stock.dal>=data['dal'] and stock.rice>=data['rice'] and stock.wheat>=data['wheat'] and stock.kerosene>=data['kerosene'] ):
                    stock.dal =  stock.dal-data['dal']
                    stock.wheat = stock.wheat-data['wheat']
                    stock.rice = stock.rice-data['rice']
                    stock.kerosene = stock.kerosene-data['kerosene']
                    stock.save()
                    ration = SoldRation.objects.create(
                        shop = request.user.shop,
                        shopid = request.user.shop.shopid,
                        dal = data['dal'],
                        rice = data['rice'],
                        wheat = data['wheat'],
                        kerosene = data['kerosene'],
                        rationid = data['rationid'],
                        date_month = today.month,
                        date_year = today.year
                    )
                    print(ration)
                    ration.save()
                    return redirect('sell')

                else:
                    messages.error(request, 'Insufficient Stock !')
                    return redirect('sell')

            
    form = Sold()
    page_obj = paginationObject(request,sales,10)
    context = {'sales':page_obj}
    return render(request,'FPS/Sell.html',context)    


@FPS_required
def Requests(request):
    today = date.today()
    
    try:
        requests = FPSRequest.objects.get(shop=request.user.shop,date_month = today.month,date_year = today.year)
        request_f = 1
    except FPSRequest.DoesNotExist:
        request_f = 0
    if request.method=='POST':
        if request.POST.get("monthly_report"):
            data = request.POST
            print('monthly')
            print(data)
            if int(data['date_month'])>today.month:
                messages.error(request,'You cannot send a report for a upcoming month !')
                return redirect('Requests')

            try:
                report = Reports.objects.get(shop=request.user.shop,date_month = data['date_month'],date_year = today.year)
            except Reports.DoesNotExist:
                report = None
            if not(report):
                report = Reports(shop=request.user.shop,date_month = today.month,date_year = today.year)
                report.save()  
                messages.success(request,'Report was successfully sent')
            else:
                messages.info(request,'Report for this month was already sent !')

            return redirect('Requests')    
        if request.POST.get("requests"):
            print("requests")   
            requests = FPSRequest(shop=request.user.shop,date_month = today.month,date_year = today.year)
            requests.save()
            request_f = 1 

    context={'requests':request_f}
    return render(request,'FPS/Requests.html',context) 
     

@FPS_required
def customers(request):
    customers = CustomerRegistration.objects.filter(shopid = request.user.shop.shopid)
    page_obj = paginationObject(request,customers,10)
    print(customers)
    context = {'customers' : page_obj}
    return render(request,'FPS/customers.html',context)      

@FPS_required
def update_status(request,pk):
    ration=RationSent.objects.get(pk=pk)
    ration.status = True
    print('saved')
    ration.save()
    if Stock.objects.filter(shop=request.user.shop).count()==0:
        stock = Stock(dal = ration.dal,wheat = ration.wheat,rice = ration.rice,kerosene = ration.kerosene,shop = request.user.shop)
        stock.save()
    else:
        stock = Stock.objects.get(shop = request.user.shop)
        stock.dal =  stock.dal+ration.dal
        stock.wheat = stock.wheat+ration.wheat
        stock.rice = stock.rice+ration.rice
        stock.kerosene = stock.kerosene+ration.kerosene
        stock.save()
    return redirect('dashboard')
    
def check_user(request):
    if request.method=='POST':
        text = request.POST.get('text')
        print(text)
        try:
            customer = CustomerRegistration.objects.get(shopid = request.user.shop.shopid,rationid =text )
        except CustomerRegistration.DoesNotExist:
            customer = None
        if customer:
            return JsonResponse({'found':1},status = 200)

    return JsonResponse({'found':0},status = 200)
           

def paginationObject(request,query,pages):
    paginator = Paginator(query, pages) # Show pages contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj