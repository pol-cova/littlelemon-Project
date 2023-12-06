from django.test import TestCase
# Import booking model
from restaurant.models import Booking

# Booking API tests
class BookingTest(TestCase):
    def test_booking(self):
        booking = Booking.objects.create(name="John", no_of_guests=5, booking_date="2021-01-01 00:00:00")
        self.assertEqual(str(booking), "John")