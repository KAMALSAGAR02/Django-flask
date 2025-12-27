from django.contrib import admin
from .models import Flight, Hotel, Booking, Passenger

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'from_city', 'to_city', 'depart_date', 'price')
    list_filter = ('from_city', 'to_city', 'depart_date')
    search_fields = ('flight_number', 'from_city', 'to_city')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'price_per_night', 'rating')
    list_filter = ('city', 'rating')
    search_fields = ('name', 'city')

class PassengerInline(admin.TabularInline):
    model = Passenger
    extra = 1

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'flight', 'hotel', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'flight__flight_number', 'hotel__name')
    inlines = [PassengerInline]
