from django.shortcuts import render,redirect,get_object_or_404
import requests
from accounts.decorators import govt_required
from django.contrib.auth.decorators import login_required
from .forms import CustomerAdd,FPSAdd,RationSend,CustomerData
from FPS.models import Reports,FPSRequest,SoldRation,Shop
from . models import RationSent,CustomerRegistration,ShopRegistration
from reportlab.pdfgen import canvas  
from django.http import HttpResponse,JsonResponse  
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import date
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
import json

# Create your views here.
months= ["January","February","March","April","May","June","July","August","September","October","November","December"]

@login_required
@govt_required
def send(request):
    context = {}
    sent = RationSent.objects.all()
    if request.method=='POST':
        form = RationSend(request.POST)
        print(context)
        if form.is_valid():
            data = form.cleaned_data
            context = {
                'dal' : data['dal'],
                'rice' : data['rice'],
                'wheat' : data['wheat'],
                'kerosene' : data['kerosene'],
                'shopid' : data['shopid'],
            }
            print(context)
            form.save()
            return redirect('send')
    form = RationSend()
    paginator = Paginator(sent, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'Govt/send.html',{'form':form,'sent':page_obj})

@login_required
@govt_required
def reports(request):
    report = Reports.objects.all()
    paginator = Paginator(report, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'reports': page_obj}
    return render(request,'Govt/reports.html',context)

@login_required
@govt_required
def orders(request):
    order = FPSRequest.objects.all()
    paginator = Paginator(order, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'orders':page_obj}
    return render(request,'Govt/orders.html',context)   

@login_required
@govt_required
def people(request):
    
    today = date.today()
    generalData = {}
    dataSearch = {}
    info = {}
    if request.method=='POST':
        print('people')
        form = CustomerData(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ration_id = data['rationid'] 
            print('is valid')
            if request.POST.get("dataSearch"):
                print('dataserach')
                try:
                    dataSearch = SoldRation.objects.get(rationid = ration_id,date_month = data['date_month'],date_year = data['date_year'])
                except SoldRation.DoesNotExist:
                    dataSearch = None

                try:
                    info = CustomerRegistration.objects.get(rationid = ration_id)
                except CustomerRegistration.DoesNotExist:
                    info = None

                try:
                    generalData = SoldRation.objects.get(rationid = ration_id,date_month = today.month,date_year = today.year)
                except SoldRation.DoesNotExist:
                    generalData = None
                
                
                

            if request.POST.get("generalData"):
                print('genraldata')
                try:
                    info = CustomerRegistration.objects.get(rationid = ration_id)
                except CustomerRegistration.DoesNotExist:
                    info = None

                try:
                    generalData = SoldRation.objects.get(rationid = ration_id,date_month = today.month,date_year = today.year)
                except SoldRation.DoesNotExist:
                    generalData = None

    else:
        form = CustomerData()   

    print('info : ')
    print(info)   
    return render(request,'Govt/people.html',{'form':form,'generalData':generalData,'info':info,'dataSearch':dataSearch})

@login_required
@govt_required
def add(request):
    context = {}
    if request.method=='POST':
        form1 = CustomerAdd(request.POST)
        form2 = FPSAdd(request.POST)
        print(context)
        if form1.is_valid():
            data = form1.cleaned_data
            context = {
                'fname' : data['fname'],
                'lname' : data['lname'],
                'address' : data['address'],
                'rationid' : data['rationid'],
                'shopid' : data['shopid'],
                'fire_otp' : data['fire_otp']
            }
            print(context)
            form1.save()
            return redirect('add')
        if form2.is_valid():
            data = form2.cleaned_data
            context = {
                'sname' : data['sname'],
                'address' : data['address'],
                'shopid' : data['shopid'],
                'secret_code' : data['secret_code']
            }
            print(context)
            form2.save()
            return redirect('add')
    
    form1 = CustomerAdd()
    form2 = FPSAdd()
    return render(request,'Govt/add.html',{'form1':form1,'form2':form2})    




# def getpdf(request,pk):  
#     text = pk
#     response = HttpResponse(content_type='application/pdf')  
#     response['Content-Disposition'] = 'inline; filename="file.pdf"'  
#     p = canvas.Canvas(response)  
#     p.setFont("Times-Roman", 55)  
#     p.drawString(100,700, text)  
#     p.showPage()  
#     p.save()  
#     return response  


 
def showPdf(request,shop,month,year):
    pdfTitle = 'Report for {} : {}'.format(months[month-1],shop)
    ration = SoldRation.objects.filter(shopid=shop,date_month=month,date_year=year)
    rations=[['Ration Id', 'Date', 'Wheat','Dal','Rice','Kerosene']]
    for item in ration:
        rations.append([item.rationid,item.date,item.wheat,item.dal,item.rice,item.kerosene])
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'inline; filename="'+pdfTitle+'.pdf"' 
    filename = 'pdftable.pdf'
    data = [['RationId', 'Date', 'Wheat','Dal','Rice','Kerosene'], ['43g4hthr', '26 April', 12,34,34,34], ['43g4hthr', '26 April', 12,34,34,34], ['43g4hthr', '26 April', 12,34,34,34]]
    pdf = SimpleDocTemplate(response,rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=72,title=pdfTitle) 
    table = Table(rations,80,30)
    # set style
    style = TableStyle([
        ('BACKGROUND',(0,0),(5,0),colors.black),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,0),14),
        ('BOTTOMPADDING',(0,0),(-1,0),12)
    ])
    # add borders
    abc = TableStyle([
        ('BOX',(0,0),(-1,-1),1,colors.black),
        # ('LINBEFORE'),
        # ('LINEABOVE'),
        ('GRID',(0,1),(-1,-1),1,colors.black)
    ])
    table.setStyle(abc)
    table.setStyle(style)
    elems = []
    elems.append(table)
    pdf.build(elems)
    return response


    

def searchReport(request):
    if request.method=='POST':
        data = request.POST
        month = data.get('month')
        year = data.get('year')
        shop_id = data.get('rationid')
        print(month)
        print(year)
        try:
            shop = Shop.objects.get(shopid = shop_id )   
        except Shop.DoesNotExist:
            return JsonResponse({'found':0},status = 200)
        if month and year:
            print('not empty')
            try:
                report = Reports.objects.get(shop = shop,date_month = month,date_year = year)
            except Reports.DoesNotExist:
                report = None
            if report:
                report_data = {
                    "shopid" : shop.shopid,
                    "shopname" : getShopName(shop.shopid),
                    "date_month":report.date_month,
                    "date_year":report.date_year,


                }
               
                report_data = json.dumps(report_data)
                report_data = json.loads(report_data)
                print(report_data)
                return JsonResponse({'found':1,'report_data':report_data},status = 200)

        

    return JsonResponse({'found':0},status = 200)



def getShopName(value):
    shop = ShopRegistration.objects.get(shopid = value)
    return shop.sname 