from django import template
from Govt.models import ShopRegistration
register = template.Library()

@register.filter
def getShopName(value):
    shop = ShopRegistration.objects.get(shopid = value)
    return shop.sname 
