from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import MyUserManager
from phonenumber_field.modelfields import PhoneNumberField
from .event import Event


class RegisteredUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(verbose_name='first name', max_length=150)
    last_name = models.CharField(verbose_name='last name', max_length=150)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True)
    phone_number = PhoneNumberField(verbose_name='phone number')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    interested_events = models.ManyToManyField(
        Event,
        db_table='user_interested_events',
        related_name='interested_users'
    )
    going_events = models.ManyToManyField(
        Event,
        db_table='user_going_events',
        related_name='going_users'
    )
    attended_events = models.ManyToManyField(
        Event,
        db_table='user_attended_events',
        related_name='attended_users'
    )
    # TODO hosted_events
    # TODO invited_events

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email
