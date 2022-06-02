'''
Series of tests checking relationship across models.
See test_<model>.py for tests related to model functionality.

# Sample objects for convenience
Customer.objects.create(first_name='Noah', last_name='Gibbs', phone_number='14039236543',email='noahark@gmail.com',address='31 hamstring drive oklahoma')
Customer(first_name='Liam', last_name='Watts', phone_number='14039876543',email='lwatt@gmail.ce',address='23 holy st los angeles')
Vehicle(vin='WAUWGAFB0C0018472',year=2012,make='Audi',model='A4',mileage=234321)
Vehicle(vin='JHMGE8G67AC003016',year=2010,make='Honda',model='Fit',mileage=163455)
'''

from random import randint
from django.test import TestCase
from bhs_app.models import Customer, RepairOrder, Vehicle

class ModelRelationshipTest(TestCase):
    '''Tests relationships between models.'''
    def setUp(self) -> None:
        Customer.objects.create(
            first_name = 'Girard',
            last_name = 'Aquino',
            phone_number = '14037144007',
            email = 'girard.aquino@email.com',
            address = '16 walgrove mews se calgary'
        )
        Customer.objects.create(
            first_name = 'Denise',
            last_name = 'Aquino',
            phone_number = '14036672458',
            email = 'denise.aquino@email.com',
            address = '16 walgrove mews se calgary'
        )
        Customer.objects.create(
            first_name = 'Denise',
            last_name = 'Richards',
            phone_number = '18542766304',
            email = 'denise.richards@emaildomain.com',
            address = '37 hollywood dr los angeles california'
        )
    
    def test_create_new_customer(self) -> None:
        '''Test customer attributes'''
        girarda = Customer.objects.get(phone_number=14037144007)
        denisea = Customer.objects.get(phone_number=14036672458)
        deniser = Customer.objects.get(phone_number=18542766304)
        
        girarda.save()
        denisea.save()
        deniser.save()

        self.assertEqual(girarda.first_name, 'Girard')
        self.assertEqual(denisea.last_name, 'Aquino')
        self.assertEqual(deniser.address, '37 hollywood dr los angeles california')
        self.assertIsNotNone(girarda.pk)
        self.assertIsNotNone(denisea.pk)
        self.assertIsNotNone(deniser.pk)
        

    def test_assign_vehicle_to_customer(self) -> None:
        '''Test vehicle relationship'''

        # Create Customer objects
        girarda = Customer.objects.get(phone_number=14037144007)
        denisea = Customer.objects.get(phone_number=14036672458)
        deniser = Customer.objects.get(phone_number=18542766304)

        girarda.save()
        denisea.save()
        deniser.save()

        # Create Vehicle objects
        Vehicle.objects.create(
            customer = girarda,
            vin = 'JH4DA1745GS002661',
            year = 1986,
            make = 'Acura',
            model = 'Integra',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = denisea,
            vin = 'WBAGH83401DP17574',
            year = 2001,
            make = 'BMW',
            model = '7 Series',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = deniser,
            vin = '1FAHP3FNXAW231964',
            year = 2010,
            make = 'Ford',
            model = 'Focus',
            mileage = randint(25000, 250000)
        )

        v1 = Vehicle.objects.get(vin='JH4DA1745GS002661')
        v2 = Vehicle.objects.get(vin='WBAGH83401DP17574')
        v3 = Vehicle.objects.get(vin='1FAHP3FNXAW231964')

        v1.save()
        v2.save()
        v3.save()

        # Check that vehicle owner is correct.
        self.assertEqual(v1.customer, girarda)
        self.assertEqual(v2.make, 'BMW')
        self.assertEqual(v3.vin, '1FAHP3FNXAW231964')
    
    def test_create_repair_order_no_vehicle(self) -> None:
        '''Test repair order relationship'''
        deniser = Customer.objects.get(phone_number=18542766304)
        deniser.save()
        ro1 = RepairOrder.objects.create(
            customer = deniser,
        )
        ro1.save()
    
    def test_create_repair_order_with_vehicle(self) -> None:
        '''Test repair order relationship'''
        pass

    def test_create_comment_for_repair_order(self) -> None:
        '''Test creating comment for repair order'''
        pass