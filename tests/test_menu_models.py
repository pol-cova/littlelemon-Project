# Here are the test for the API endpoints 
from django.test import TestCase
# Import models from restaurant app
from restaurant.models import Menu, Booking

# Menu API tests
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)   
        self.assertEqual(str(item), "IceCream : 80")