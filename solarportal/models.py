from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import *

#### Irrigation models
class Watering(models.Model):



#### Weather models
class MeasurementNode(models.Model):
    serial_number = models.CharField(max_length=20)
    created = models.DateTimeField('Datetime node was created')
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')


class Temperature(models.Model):
    measurement_node = models.ForeignKey(MeasurementNode)
    measurement_datetime = models.DateTimeField('Time temperature was measured')
    measurement_value = models.DecimalField('Temperature value', max_digits=5, decimal_places=2)


class Wind(models.Model):
    measurement_datetime = models.DateTimeField('Time wind was measured')
    speed_value = models.DecimalField('Wind speed', max_digits=5, decimal_places=2)
    direction_value = models.PositiveSmallIntegerField('Wind direction')


class Rain(models.Model):
    measurement_datetime = models.DateTimeField('Datetime rainfall was measured')
    measurement_duration = models.DurationField('Length rainfall was measured')
    measurement_value = models.PositiveSmallIntegerField('Amount of rainfall')
