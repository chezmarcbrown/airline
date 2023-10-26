from django.db import models

class Flight1(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination} ({self.duration})'
    
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.TextField()
    
    def __str__(self):
        return f'{self.city} ({self.code})'
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination} ({self.duration})'

class Passenger(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    # The `flights` field in the `Passenger` model is a `ManyToManyField` that establishes a
    # many-to-many relationship between the `Passenger` and `Flight` models. This means that a
    # passenger can be associated with multiple flights, and a flight can have multiple passengers.
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')
    
    def __str__(self):
        return f'{self.first} {self.last}'