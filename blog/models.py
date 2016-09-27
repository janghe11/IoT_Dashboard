from __future__ import unicode_literals

from django.db import models
from chartit import DataPool, Chart

# Create your models here.
class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
        return str(self.month)