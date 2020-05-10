from django.contrib import admin
from .models import Shop,Stock,FPSRequest,Reports,SoldRation
# Register your models here.
admin.site.register(Shop)
admin.site.register(Stock)
admin.site.register(FPSRequest)
admin.site.register(Reports)
admin.site.register(SoldRation)
