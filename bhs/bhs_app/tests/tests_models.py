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
from bhs_app.models import Comments, Customer, RepairOrder, Vehicle

class ModelRelationshipTest(TestCase):
    '''Tests relationships between models.
    TODO:
    - Sanitize tests
    '''
    def setUp(self) -> None:
        Customer.objects.create(
            first_name = 'Ojigkwanong',
            last_name = 'Cavan',
            phone_number = '15823338105',
            email = 'OjigkwanongC@gmail.com',
            address = '2629 Yonge Street Toronto Ontario'
        )
        Customer.objects.create(
            first_name = 'Drupada',
            last_name = 'Spellmeyer',
            phone_number = '13109996564',
            email = 'drupspell@yahoo.ca',
            address = '2629 Yonge Street Toronto Ontario'
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
        c1 = Customer.objects.get(phone_number=15823338105)
        c2 = Customer.objects.get(phone_number=13109996564)
        c3 = Customer.objects.get(phone_number=18542766304)
        c1.save()
        c2.save()
        c3.save()

        self.assertIsInstance(c1, Customer)
        self.assertIsInstance(c2, Customer)
        self.assertIsInstance(c3, Customer)

        self.assertEqual(c1.first_name, 'Ojigkwanong')
        self.assertEqual(c1.last_name, 'Cavan')
        self.assertEqual(c1.phone_number, 15823338105)
        self.assertEqual(c1.email, 'OjigkwanongC@gmail.com')
        self.assertEqual(c1.address, '2629 Yonge Street Toronto Ontario')

        self.assertEqual(c2.first_name, 'Drupada')
        self.assertEqual(c2.last_name, 'Spellmeyer')
        self.assertEqual(c2.phone_number, 13109996564)
        self.assertEqual(c2.email, 'drupspell@yahoo.ca')
        self.assertEqual(c2.address, '2629 Yonge Street Toronto Ontario')

        self.assertEqual(c3.first_name, 'Denise')
        self.assertEqual(c3.last_name, 'Richards')
        self.assertEqual(c3.phone_number, 18542766304)
        self.assertEqual(c3.email, 'denise.richards@emaildomain.com')
        self.assertEqual(c3.address, '37 hollywood dr los angeles california')

        self.assertIsNotNone(c1.pk)
        self.assertIsNotNone(c2.pk)
        self.assertIsNotNone(c3.pk)

    def test_assign_vehicle_to_customer(self) -> None:
        '''Test vehicle relationship'''

        # Create Customer objects
        c1 = Customer.objects.get(phone_number=15823338105)
        c2 = Customer.objects.get(phone_number=13109996564)
        c3 = Customer.objects.get(phone_number=18542766304)
        c1.save()
        c2.save()
        c3.save()
         
        # Create Vehicle objects
        Vehicle.objects.create(
            customer = c1,
            vin = 'JH4DA1745GS002661',
            year = 1986,
            make = 'Acura',
            model = 'Integra',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c2,
            vin = 'WBAGH83401DP17574',
            year = 2001,
            make = 'BMW',
            model = '7 Series',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c3,
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
        self.assertIsInstance(v1, Vehicle)
        self.assertEqual(v1.customer, c1)
        self.assertEqual(v1.vin, 'JH4DA1745GS002661')
        self.assertEqual(v1.year, 1986)
        self.assertEqual(v1.make, 'Acura')
        self.assertEqual(v1.model, 'Integra')

        self.assertIsInstance(v2, Vehicle)
        self.assertEqual(v2.customer, c2)
        self.assertEqual(v2.vin, 'WBAGH83401DP17574')
        self.assertEqual(v2.year, 2001)
        self.assertEqual(v2.make, 'BMW')
        self.assertEqual(v2.model, '7 Series')

        self.assertIsInstance(v3, Vehicle)
        self.assertEqual(v3.customer, c3)
        self.assertEqual(v3.vin, '1FAHP3FNXAW231964')
        self.assertEqual(v3.year, 2010)
        self.assertEqual(v3.make, 'Ford')
        self.assertEqual(v3.model, 'Focus')
    
    def test_assign_multiple_vehicles_to_customer(self) -> None:
        '''Test many vehicles to one customer relationship'''

        # Create Customer object
        c1 = Customer.objects.get(phone_number=15823338105)
        c1.save()
         
        # Create Vehicle objects
        Vehicle.objects.create(
            customer = c1,
            vin = 'JH4DA1745GS002661',
            year = 1986,
            make = 'Acura',
            model = 'Integra',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c1,
            vin = 'WBAGH83401DP17574',
            year = 2001,
            make = 'BMW',
            model = '7 Series',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c1,
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
        self.assertIsInstance(v1, Vehicle)
        self.assertEqual(v1.customer, c1)
        self.assertEqual(v1.vin, 'JH4DA1745GS002661')
        self.assertEqual(v1.year, 1986)
        self.assertEqual(v1.make, 'Acura')
        self.assertEqual(v1.model, 'Integra')

        self.assertIsInstance(v2, Vehicle)
        self.assertEqual(v2.customer, c1)
        self.assertEqual(v2.vin, 'WBAGH83401DP17574')
        self.assertEqual(v2.year, 2001)
        self.assertEqual(v2.make, 'BMW')
        self.assertEqual(v2.model, '7 Series')

        self.assertIsInstance(v3, Vehicle)
        self.assertEqual(v3.customer, c1)
        self.assertEqual(v3.vin, '1FAHP3FNXAW231964')
        self.assertEqual(v3.year, 2010)
        self.assertEqual(v3.make, 'Ford')
        self.assertEqual(v3.model, 'Focus')


    def test_create_repair_order_no_vehicle(self) -> None:
        '''Test repair order relationship with customer with no vehicle'''
        c1 = Customer.objects.get(phone_number=15823338105)
        c2 = Customer.objects.get(phone_number=13109996564)
        c3 = Customer.objects.get(phone_number=18542766304)
        c1.save()
        c2.save()
        c3.save()

        ro1 = RepairOrder.objects.create(customer=c1)
        ro2 = RepairOrder.objects.create(customer=c2)
        ro3 = RepairOrder.objects.create(customer=c3)
        ro1.save()
        ro2.save()
        ro3.save()

        self.assertIsInstance(ro1, RepairOrder)
        self.assertIsNotNone(ro1.pk)
        self.assertIsNone(ro1.vin)
        
        self.assertIsInstance(ro2, RepairOrder)
        self.assertIsNotNone(ro2.pk)
        self.assertIsNone(ro2.vin)
        
        self.assertIsInstance(ro3, RepairOrder)
        self.assertIsNotNone(ro3.pk)
        self.assertIsNone(ro3.vin)

    def test_create_repair_order_with_vehicle(self) -> None:
        '''Test repair order relationship with customer with vehicle'''
        # Create Vehicle objects
        c1 = Customer.objects.get(phone_number=15823338105)
        c2 = Customer.objects.get(phone_number=13109996564)
        c3 = Customer.objects.get(phone_number=18542766304)
        c1.save()
        c2.save()
        c3.save()

        Vehicle.objects.create(
            customer = c1,
            vin = 'JH4DA1745GS002661',
            year = 1986,
            make = 'Acura',
            model = 'Integra',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c2,
            vin = 'WBAGH83401DP17574',
            year = 2001,
            make = 'BMW',
            model = '7 Series',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c3,
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

        ro1 = RepairOrder.objects.create(customer=c1)
        ro2 = RepairOrder.objects.create(customer=c2)
        ro3 = RepairOrder.objects.create(customer=c3)
        ro1.save()
        ro2.save()
        ro3.save()

        self.assertIs(c1.customer, v1.customer_id)
        self.assertIs(c2.customer, v2.customer_id)
        self.assertIs(c3.customer, v3.customer_id)
        self.assertIs(c1.customer, ro1.customer_id)
        self.assertIs(c2.customer, ro2.customer_id)
        self.assertIs(c3.customer, ro3.customer_id)
        self.assertIs(v1.customer_id, ro1.customer_id)
        self.assertIs(v2.customer_id, ro2.customer_id)
        self.assertIs(v3.customer_id, ro3.customer_id)

        self.assertEqual(c1.pk, ro1.customer_id)
        self.assertEqual(c2.pk, ro2.customer_id)
        self.assertEqual(c3.pk, ro3.customer_id)
        self.assertEqual(ro1.customer_id, v1.customer_id)
        self.assertEqual(ro2.customer_id, v2.customer_id)
        self.assertEqual(ro3.customer_id, v3.customer_id)

    def test_create_comment_for_repair_order(self) -> None:
        '''Test creating comment for repair order'''
        # Create objects
        c1 = Customer.objects.get(phone_number=15823338105)
        c2 = Customer.objects.get(phone_number=13109996564)
        c3 = Customer.objects.get(phone_number=18542766304)
        c1.save()
        c2.save()
        c3.save()

        Vehicle.objects.create(
            customer = c1,
            vin = 'JH4DA1745GS002661',
            year = 1986,
            make = 'Acura',
            model = 'Integra',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c2,
            vin = 'WBAGH83401DP17574',
            year = 2001,
            make = 'BMW',
            model = '7 Series',
            mileage = randint(25000, 250000)
        )
        Vehicle.objects.create(
            customer = c3,
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

        ro1 =RepairOrder.objects.create(customer=c1)
        ro2 =RepairOrder.objects.create(customer=c2)
        ro3 =RepairOrder.objects.create(customer=c3)

        co1 = Comments.objects.create(
            comment="Hello world.",
            ro=ro1,
            job_description = "sample text",
            error_codes = "sample text",
            amount_total = 500.00,
        )
        co2 = Comments.objects.create(
            comment="Hello world.",
            ro=ro2,
            job_description = "sample text",
            error_codes = "sample text",
            amount_total = 500.00
        )
        co3 = Comments.objects.create(
            comment="Hello world.",
            ro=ro3,
            job_description = "sample text",
            error_codes = "sample text",
            amount_total = 500.00
        )
        co1.save()
        co2.save()
        co3.save()

        self.assertIsNotNone(co1.ro_id)
        self.assertIsNotNone(co2.ro_id)
        self.assertIsNotNone(co3.ro_id)

        self.assertIs(co1.ro_id, ro1.pk)
        self.assertIs(co2.ro_id, ro2.pk)
        self.assertIs(co3.ro_id, ro3.pk)