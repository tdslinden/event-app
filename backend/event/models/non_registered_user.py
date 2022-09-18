from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from event.models import Event


class NonRegisteredUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
