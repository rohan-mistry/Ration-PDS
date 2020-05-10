from django import template
from Govt.models import CustomerRegistration
register = template.Library()

@register.filter
def getCustomerName(value):
    customer = CustomerRegistration.objects.get(rationid = value)
    return "{} {}".format(customer.fname, customer.lname) 
