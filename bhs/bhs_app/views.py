import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm, VehicleForm
from . import models
from . import managers

def index(request):
    return render(request, 'bhs_app/index.html')

def login(request):
    return render(request, 'bhs_app/login.html')

@login_required(login_url='login')
def create_new_customer(request):
    '''Form to create an entry'''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form = CustomerForm()
    return render(request, 'bhs_app/create_new_customer.html', {'form': form})

@login_required(login_url='login')
def search(request):
    '''Search the database
    TODO:
    - default outputs all() due to managers.py; maybe output max 10 sorted by
    created recently?
    - catch non-GET request method and throw error? for security?
    '''
    if request.method == 'GET':
        q = request.GET.get('q')
        if q == None:
            data = None
        else:
            data = models.Customer.objects.all().filter(phone_number__icontains=q)
    return render(request, 'bhs_app/search.html', {'data': data})

@login_required(login_url='login')
def view_customers(request):
    '''Display data on webpage
    TODO:
    - limit number of row items
    '''
    all_customer_data = managers.AllCustomers.all_customers
    return render(request, 'bhs_app/view_customers.html',
                 {'data': list(all_customer_data)})

@login_required(login_url='login')
def view_customer_profile(request, customer_id):
    '''Display customer profile page
    '''    
    customer = models.Customer.objects.all().filter(pk=customer_id)
    return render(request, 'bhs_app/view_customer_profile.html', {'data': customer})

@login_required(login_url='login')
def thanks(request):
    return render(request, 'bhs_app/thanks.html')