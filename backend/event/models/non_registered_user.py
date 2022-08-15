from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class NonRegisteredUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
