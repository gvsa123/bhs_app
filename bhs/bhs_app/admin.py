from django.contrib import admin
from .models import Customer, Vehicle, RepairOrder, Comments

# Register your models here.
admin.site.register([Customer, Vehicle, RepairOrder, Comments])