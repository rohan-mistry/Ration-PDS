from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from . models import User
from FPS.models import Shop
from Customer.models import Customer
from Govt.models import CustomerRegistration,ShopRegistration

class FPSSignUpForm(UserCreationForm):
    shop_name = forms.CharField(max_length=20,widget= forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'enter a text'
        }
    ))
    shopid = forms.CharField(max_length=20)
    secret_code = forms.CharField(max_length=10)
    class Meta(UserCreationForm.Meta):
        model = User
       

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        try:
            fps = ShopRegistration.objects.get(shopid = data['shopid'],secret_code = data['secret_code'])
        except ShopRegistration.DoesNotExist:
            fps = None  
        if not(fps):
            user  = None
            return user
            
        else:       
            user.is_FPS = True
            user.save()
            student  = Shop.objects.create(user = user,shopid= data['shopid'],shop_name= data['shop_name'])
            return user

            

class CustomerSignUpForm(UserCreationForm):
    ration_id = forms.CharField(max_length=15)
    shop_id = forms.CharField(max_length=15)
    address = forms.CharField(max_length=200)
    fire_otp = forms.IntegerField()
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        try:
            customer = CustomerRegistration.objects.get(rationid = data['ration_id'],fire_otp = data['fire_otp'])
        except CustomerRegistration.DoesNotExist:
            customer = None 
        if not(customer):
            user  = None
            return user
        else:
            user.is_customer = True
            user.save()
            student  = Customer.objects.create(user = user,ration_id= data['ration_id'],shop_id= data['shop_id'],address= data['address'])
            return user



    