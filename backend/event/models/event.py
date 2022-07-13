# Create your models here.
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    photo_link = models.CharField(max_length=1000, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)