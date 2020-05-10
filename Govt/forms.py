from django.forms import ModelForm
from django import forms
from .models import CustomerRegistration,ShopRegistration,RationSent
class CustomerAdd(ModelForm):
    class Meta:
        model = CustomerRegistration
        fields = '__all__'

class FPSAdd(ModelForm):
    class Meta:
        model = ShopRegistration
        fields = '__all__' 

class RationSend(ModelForm):
    class Meta:
        model = RationSent
        fields = ['shopid','wheat','dal','kerosene','rice'] 

class CustomerData(forms.Form):
    rationid = forms.CharField(max_length = 20)
    date_month = forms.IntegerField(required = False)
    date_year = forms.IntegerField(required = False)
    
