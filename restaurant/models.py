from django.db import models

# Restaurant api models

# Menu Model 
# title: varchar(255), price: decimal(10, 2), inventory: int(5) 
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_item(self):
        return f'{self.title} : {self.price}'

# Booking Model
# name: varchar(255), no_of_guests: int(6), BookingDate: datetime
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name