from django.db import models
from accounts.models import User
# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=20)
    shopid = models.CharField(max_length=20)

    def __str__(self):
        return self.shop_name


class Stock(models.Model):
    wheat = models.IntegerField()
    rice = models.IntegerField()
    dal = models.IntegerField()
    kerosene = models.IntegerField()
    # shopid = models.CharField(max_length=20,default='SOME STRING')
    shop = models.OneToOneField(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.shop.shop_name  
    
class FPSRequest(models.Model):
    # shopid = models.CharField(max_length=20)
    date  = models.DateField(auto_now=True)
    date_month = models.IntegerField(null=True,blank = True)
    date_year = models.IntegerField(null=True,blank = True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.shop.shop_name 

class Reports(models.Model):
    # shopid = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    date_month = models.IntegerField(null=True,blank = True)
    date_year = models.IntegerField(null=True,blank = True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.shop.shop_name 

class SoldRation(models.Model):
    date = models.DateField(auto_now=True)
    rationid = models.CharField(max_length = 15)
    shopid = models.CharField(max_length = 20,null=True,blank = True)
    wheat = models.IntegerField()
    rice = models.IntegerField()
    dal = models.IntegerField()
    kerosene = models.IntegerField()
    date_month = models.IntegerField(null=True,blank = True)
    date_year = models.IntegerField(null=True,blank = True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.shop.shop_name






