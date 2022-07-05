from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    date_of_birth = models.DateTimeField()
    phone_number = PhoneNumberField()
