from django.db import models
from django.contrib.auth.models import User
import datetime

# Flight Model
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    depart_date = models.DateField(default=datetime.date.today)
    return_date = models.DateField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.flight_number}: {self.from_city} → {self.to_city}"

# Hotel Model
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    price_per_night = models.FloatField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - {self.city}"

# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(('Confirmed', 'Confirmed'), ('Pending', 'Pending')))

    def __str__(self):
        return f"Booking {self.id} - {self.user.username}"

# Optional: Passenger details for flights
class Passenger(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
