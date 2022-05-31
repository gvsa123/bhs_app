from django.test import TestCase
from bhs_app.models import Customer

class CustomerTestCase(TestCase):
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
    
    def test_create_new_customer(self):
        '''Test creating a new customer without a vehicle'''
        girarda = Customer.objects.get(phone_number=14037144007)
        denisea = Customer.objects.get(phone_number=14036672458)
        deniser = Customer.objects.get(phone_number=18542766304)
        self.assertEqual(girarda.first_name, 'Girard')
        self.assertEqual(denisea.last_name, 'Aquino')
        self.assertEqual(deniser.address, '37 hollywood dr los angeles california')