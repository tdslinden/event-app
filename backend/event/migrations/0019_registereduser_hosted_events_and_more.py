# Generated by Django 4.0.5 on 2022-08-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0018_remove_nonregistereduser_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='hosted_events',
            field=models.ManyToManyField(db_table='user_hosted_events', related_name='hosting_users', to='event.event'),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='invited_events',
            field=models.ManyToManyField(db_table='user_invited_events', related_name='invited_users', to='event.event'),
        ),
    ]
