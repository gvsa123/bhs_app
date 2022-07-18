from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm, VehicleForm, RepairOrderForm, CommentsForm
from . import models
from . import managers

def index(request):
    return render(request, 'bhs_app/index.html')

def login(request):
    return render(request, 'bhs_app/login.html')

@login_required(login_url='login')
def create_new_customer(request):
    '''Creae a new customer'''
    if request.method == 'POST':
        form_customer = CustomerForm(request.POST)
        if form_customer.is_valid():
            form_customer.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form_customer = CustomerForm()
    return render(
        request,
        'bhs_app/create_new_customer.html',
        {'form_customer': form_customer}
    )

@login_required(login_url='login')
def create_new_vehicle(request, customer_id):
    '''Create a new vehicle
    TODO:
    -   populate form with initial={'customer': customer_obj}
    '''
    # get customer
    current_customer = managers.AllCustomers.all_customers.filter(pk=customer_id)

    if request.method == 'POST':
        form_vehicle = VehicleForm(request.POST)
        form_vehicle.instance.customer = current_customer[0]

        if form_vehicle.is_valid():
            form_vehicle.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form_vehicle = VehicleForm()

    return render(
        request, 'bhs_app/create_new_vehicle.html',
        {'form_vehicle': form_vehicle, 'data': customer_id}
    )

@login_required(login_url='login')
def create_new_repair_order(request, customer_id):
    '''Create a repair order
    TODO:
    - fix -> NOT NULL constraint customer_id
    '''
    customer = models.Customer.objects.all().filter(pk=customer_id)

    if request.method == 'POST':
        form_repair_order = RepairOrderForm(request.POST)
        if form_repair_order.is_valid():
            form_repair_order.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form_repair_order = RepairOrderForm()
    return render(
        request, 'bhs_app/create_new_repair_order.html',
        {'form_repair_order': form_repair_order,'data': customer}
    )

@login_required(login_url='login')
def create_new_comment(request, customer_id):
    '''Create a comment.
    TODO:
    - fix -> NOT NULL constraint customer_id
    '''
    customer = models.Customer.objects.all().filter(pk=customer_id)

    if request.method == 'POST':
        form_comment = CommentsForm(request.POST)
        if form_comment.is_valid():
            form_comment.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form_comment = CommentsForm()
    return render(
        request, 'bhs_app/create_new_comment.html',
        {'form_comment': form_comment,'data': customer}
    )

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
    '''Display customer profile page'''
    customer = models.Customer.objects.all().filter(pk=customer_id)
    customer_vehicles = managers.AllVehicles.all_vehicles.filter(
        customer=customer[0]
    )
    return render(
        request,
        'bhs_app/view_customer_profile.html',
        {
            'data_customer': customer,
            'data_vehicle': customer_vehicles,
            'customer_id': customer_id
        }
    )

@login_required(login_url='login')
def thanks(request):
    return render(request, 'bhs_app/thanks.html')