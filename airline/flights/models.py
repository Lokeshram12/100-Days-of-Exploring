from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name='departure', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.duration} minutes)"