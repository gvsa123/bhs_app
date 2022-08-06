# import datetime
# from datetime import datetime
# from distutils.archive_util import make_archive
# from pyexpat import model
# from tkinter import CASCADE
from django.db import models
from datetime import date

'''
TODO:
-   format admin page output; modelAdmin.field.
-   refactor model class __str__ methods.
'''


class Customer(models.Model):
    '''Basic customer information.'''

    customer = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.BigIntegerField(unique=True)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        fullname = self.last_name + ', ' + self.first_name
        return fullname


class Vehicle(models.Model):
    '''Relevant vehicle information
    TODO:
    -   check https://www.back4app.com/database/how-it-works;
        create model dictionary OR use api?

    '''
    YTD = date.today().year + 1
    YEARS = [(yr, yr) for yr in range(1980, YTD, 1)]

    # List of car manufacturers
    MFR = [
        ("Abarth", "Abarth"),
        ("Alfa Romeo", "Alfa Romeo"),
        ("Aston Martin", "Aston Martin"),
        ("Audi", "Audi"),
        ("Bentley", "Bentley"),
        ("BMW", "BMW"),
        ("Bugatti", "Bugatti"),
        ("Cadillac", "Cadillac"),
        ("Chevrolet", "Chevrolet"),
        ("Chrysler", "Chrysler"),
        ("Citroën", "Citroën"),
        ("Dacia", "Dacia"),
        ("Daewoo", "Daewoo"),
        ("Daihatsu", "Daihatsu"),
        ("Dodge", "Dodge"),
        ("Donkervoort", "Donkervoort"),
        ("DS", "DS"),
        ("Ferrari", "Ferrari"),
        ("Fiat", "Fiat"),
        ("Fisker", "Fisker"),
        ("Ford", "Ford"),
        ("Honda", "Honda"),
        ("Hummer", "Hummer"),
        ("Hyundai", "Hyundai"),
        ("Infiniti", "Infiniti"),
        ("Iveco", "Iveco"),
        ("Jaguar", "Jaguar"),
        ("Jeep", "Jeep"),
        ("Kia", "Kia"),
        ("KTM", "KTM"),
        ("Lada", "Lada"),
        ("Lamborghini", "Lamborghini"),
        ("Lancia", "Lancia"),
        ("Land Rover", "Land Rover"),
        ("Landwind", "Landwind"),
        ("Lexus", "Lexus"),
        ("Lotus", "Lotus"),
        ("Maserati", "Maserati"),
        ("Maybach", "Maybach"),
        ("Mazda", "Mazda"),
        ("McLaren", "McLaren"),
        ("Mercedes-Benz", "Mercedes-Benz"),
        ("MG", "MG"),
        ("Mini", "Mini"),
        ("Mitsubishi", "Mitsubishi"),
        ("Morgan", "Morgan"),
        ("Nissan", "Nissan"),
        ("Opel", "Opel"),
        ("Peugeot", "Peugeot"),
        ("Porsche", "Porsche"),
        ("Renault", "Renault"),
        ("Rolls-Royce", "Rolls-Royce"),
        ("Rover", "Rover"),
        ("Saab", "Saab"),
        ("Seat", "Seat"),
        ("Skoda", "Skoda"),
        ("Smart", "Smart"),
        ("SsangYong", "SsangYong"),
        ("Subaru", "Subaru"),
        ("Suzuki", "Suzuki"),
        ("Tesla", "Tesla"),
        ("Toyota", "Toyota"),
        ("Volkswagen", "Volkswagen"),
        ("Volvo", "Volvo")
    ]

    vin = models.CharField(unique=True, max_length=17)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT)
    year = models.PositiveSmallIntegerField(choices=YEARS, default=YTD)
    make = models.CharField(choices=MFR, max_length=50, null=True)
    model = models.CharField(max_length=20, null=True)
    mileage = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.vin


class RepairOrder(models.Model):
    '''Unique repair order'''

    ro = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, to_field='customer')
    vin = models.ForeignKey('Vehicle', on_delete=models.RESTRICT, null=True, to_field='vin')
    date_created = models.DateField(default=date.today, blank=False, null=False)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.ro}"


class Comments(models.Model):
    '''Comments table associated with repair order
    TODO:
    -   Add other features -> error codes, job description, etc.
    '''

    ro = models.ForeignKey('RepairOrder', on_delete=models.PROTECT, null=True, to_field='ro')
    date_modified = models.DateField(default=date.today, blank=False, null=False)
    comment = models.TextField()
