from django.forms import ModelForm
from .models import SoldRation

class Sold(ModelForm):
    class Meta:
        model = SoldRation
        fields = ['rice','dal','wheat','kerosene','rationid']

