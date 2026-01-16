from django.db import models
from django.utils import timezone

class SatelliteLog(models.Model):
    sat_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return f"{self.sat_name} tracked at {self.timestamp}"
