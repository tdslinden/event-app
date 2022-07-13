from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=150, primary_key=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    date_of_birth = models.DateTimeField()
    phone_number = PhoneNumberField(blank=False)
