from django.test import TestCase
from restaurant.models import Menu, Booking

# Create your tests here.
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        #self.assertEqual(item, "IceCream : 80")
        self.assertEqual(itemstr, "IceCream : 80")

class MenuViewTest (TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=8, inventory=10)
        Menu.objects.create(title="FrenchFrire", price=18, inventory=4)
