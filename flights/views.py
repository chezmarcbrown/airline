from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Flight

def index(request):
    return render(request, "flights/index.html",
                  { 'flights': Flight.objects.all()})

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404(f'FLight id #{flight_id} does not exist')
    return render(request, "flights/flight.html",
                  { 'flight': flight})


def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flights/flight.html",
                  { 'flight': flight,
                   'passengers': flight.passengers.all()})
