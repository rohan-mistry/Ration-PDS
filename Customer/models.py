from django.db import models
from accounts.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    ration_id = models.CharField(max_length=15)
    shop_id = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.ration_id
    
class RationData(models.Model):
    date = models.DateField(auto_now=True)
    wheat = models.IntegerField()
    rice = models.IntegerField()
    dal = models.IntegerField()
    kerosene = models.IntegerField()
    # custom_id = models.CharField(max_length=15,default='SOME STRING')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.ration_id

