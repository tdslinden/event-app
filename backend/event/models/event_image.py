from django.db import models
from event.models import Event

class EventImage(models.Model):
    title = models.CharField(max_length=255)
    image_link = models.ImageField(upload_to='media/')
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
