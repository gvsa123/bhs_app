'''
Manager code to interface with database. You need this in order to
interface with your database, and to have data to pass to your views!

TODO:
- no need for manager; delete in prod.
'''

from . import models

class AllCustomers(models.Customer):
    '''Returns all the values of model'''
    all_customers = models.Customer.objects.all() # use values()?



