from django.db import models

class Aircraft(models.Model):
    Callsign = models.CharField(max_length=15)
    Taxi = models.JSONField(null=True, default=["0"])
    Takeoff = models.CharField(max_length=10, null=True, default="0")    
    Landing = models.CharField(max_length=10, null=True, default="0")    
    lastInstruction = models.CharField(max_length=255, null=True, default=" ")