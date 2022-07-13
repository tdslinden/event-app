from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=150, primary_key=True)
    date_of_birth = models.DateTimeField()
    phone_number = PhoneNumberField()
