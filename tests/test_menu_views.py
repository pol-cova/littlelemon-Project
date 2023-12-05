# Views test
from django.test import TestCase
from django.core.serializers import serialize
import json
# import models
from restaurant.models import Menu, Booking

# MenuViewTest
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chocolate", price=100, inventory=100)
        Menu.objects.create(title="Cake", price=120, inventory=100)
    def test_getall(self):
        # Retrieve all Menu objects added for the test purpose
        menus = Menu.objects.all()

        # Serialize the retrieved objects
        serialized_data = serialize('json', menus)

        # Deserialize both expected and actual data
        expected_data = serialize('json', Menu.objects.all())
        actual_data = serialized_data

        # Deserialize the JSON strings to Python objects
        expected_objects = sorted(json.loads(expected_data), key=lambda x: x['pk'])
        actual_objects = sorted(json.loads(serialized_data), key=lambda x: x['pk'])

        # Make assertions to check if the serialized data equals the response
        self.assertEqual(expected_objects, actual_objects)
