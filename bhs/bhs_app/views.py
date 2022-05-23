import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm, VehicleForm
from . import models
from . import managers
# Create your views here.

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

    return render(request, 'bhs_app/search.html', {'search_data': data})

@login_required(login_url='login')
def view_customers(request):
    '''Display data on webpage
    TODO:
    - limit number of row items
    '''
    all_customer_data = managers.AllCustomers.all_customers
    all_customer_data_list = [i for i in all_customer_data.values_list()]
    print(f"all_customer_data --> {all_customer_data}")
    print(f"all_customer_data --> {type(all_customer_data)}")
    print(f"all_customer_data --> {dir(all_customer_data)}")
    print(f"all_customer_data_list --> {type(all_customer_data_list[0])}")
    print(f"all_customer_data_list --> {all_customer_data_list}")

    return render(request, 'bhs_app/view_customers.html',
                 {'all_customer_data': list(all_customer_data)})

@login_required(login_url='login')
def view_customer_profile(request, customer_id):
    '''Display customer profile page'''
    data = get_object_or_404(models.Customer, pk=customer_id)
    print(data)

    return render(request, 'bhs_app/view_customer_profile.html', {'customer': data.pk})

@login_required(login_url='login')
def thanks(request):
    return render(request, 'bhs_app/thanks.html')