
from django.shortcuts import render
from .models import Flight, Hotel

def flights_page(request):
    flights = Flight.objects.all()
    return render(request, 'maketrip/flights.html', {'flights': flights})

def hotels_page(request):
    hotels = Hotel.objects.all()
    return render(request, 'maketrip/hotels.html', {'hotels': hotels})

# Existing index view
def index(request):
    return render(request, 'maketrip/index.html')

# New search results view
def search_results(request):
    # Get data from GET request
    from_city = request.GET.get('from')
    to_city = request.GET.get('to')
    depart = request.GET.get('depart')
    return_date = request.GET.get('return')

    # For now, we’ll simulate results
    results = [
        {'type': 'Flight', 'name': 'AirX', 'price': '$200'},
        {'type': 'Flight', 'name': 'SkyJet', 'price': '$180'},
        {'type': 'Flight', 'name': 'FlyHigh', 'price': '$220'},
    ]

    context = {
        'from_city': from_city,
        'to_city': to_city,
        'depart': depart,
        'return_date': return_date,
        'results': results
    }
    return render(request, 'maketrip/results.html', context)
def home(request):
    return render(request, 'maketrip/home.html')