from django.contrib import admin
from .models import RationSent,CustomerRegistration,ShopRegistration

# Register your models here.
admin.site.register(RationSent)
admin.site.register(CustomerRegistration)
admin.site.register(ShopRegistration)
