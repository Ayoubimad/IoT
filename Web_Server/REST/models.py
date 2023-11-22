from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
