# Generated by Django 4.0.5 on 2022-08-15 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_registereduser_attended_events_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonregistereduser',
            name='event',
        ),
    ]
