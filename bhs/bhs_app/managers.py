# Manager code to interface with database. You need this in order to
# interface with your database, and to have data to pass to your views!

from . import models


class AllCustomers(models.Customer):
    """Returns all customers."""
    all_customers = models.Customer.objects.all()  # use values()?


class AllVehicles(models.Vehicle):
    """Retruns all vehicles."""
    all_vehicles = models.Vehicle.objects.all()


class AllRepairOrders(models.RepairOrder):
    """Returns all repair orders."""
    all_repair_orders = models.RepairOrder.objects.all()


class AllComments(models.Comments):
    """Returns all comments"""
    all_comments = models.Comments.objects.all()
