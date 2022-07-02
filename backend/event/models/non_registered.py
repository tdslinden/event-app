from pyexpat import model
from django.db import models
from .event import Event

class NonRegisteredUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255) #TODO: change to phonenumber_field
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
