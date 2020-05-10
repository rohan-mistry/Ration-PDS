from django.db import models

# Create your models here.
class RationSent(models.Model):
    shopid = models.CharField(max_length=15)
    wheat = models.IntegerField()
    rice = models.IntegerField()
    dal = models.IntegerField()
    kerosene = models.IntegerField()
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.shopid

class CustomerRegistration(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    rationid = models.CharField(max_length=15)
    shopid = models.CharField(max_length=15)
    fire_otp = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.rationid

class ShopRegistration(models.Model):
    sname = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    shopid = models.CharField(max_length=15)
    secret_code = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.shopid



        