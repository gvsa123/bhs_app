from dataclasses import fields
from django.forms import ModelForm
from . import models

# Create forms based on your model
class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

class VehicleForm(ModelForm):
    class Meta:
        model = models.Vehicle
        fields = ['vin', 'year', 'make', 'model', 'mileage']

class RepairOrderForm(ModelForm):
    class Meta:
        model = models.RepairOrder
        fields = ['ro','date','completed']

class CommentsForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['date', 'comment']