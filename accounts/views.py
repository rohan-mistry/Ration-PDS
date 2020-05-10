from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from . forms import FPSSignUpForm
from . forms import CustomerSignUpForm
from . models import User
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages



class FPSSignUpView(CreateView):
    model = User
    form_class = FPSSignUpForm
    template_name = 'registration/FPS_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['data'] = {'type':'FPS'}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        if not(user):
            messages.error(self.request,'Sorry! You are not verified by Government')
            return redirect('FPS_signup')
            
        login(self.request, user)
        return redirect('dashboard')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['data'] = {'type':'Customer'}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        if not(user):
            messages.error(self.request,'Sorry! You are not verified by Government')
            return redirect('Customer_signup')
        login(self.request, user)
        return redirect('detail')        



def home(request):
    if request.user.is_authenticated:
        if request.user.is_FPS:
            return redirect('dashboard')
        elif request.user.is_customer:
            return redirect('detail')
        else:
            return redirect('send')
    return redirect('login')  

def demo(request):
    return render(request,'registration/login1.html')

  
    