from django.db import models
import pytz

# Create your models here.
class User(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(max_length=20, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    #activity_periods = models.ForeignKey('ActivityPeriod', on_delete=models.CASCADE)

class ActivityPeriod(models.Model):
    ids = models.CharField(max_length=20,null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()