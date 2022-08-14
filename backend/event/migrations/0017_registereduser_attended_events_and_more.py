# Generated by Django 4.0.5 on 2022-08-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_merge_20220805_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='attended_events',
            field=models.ManyToManyField(db_table='user_attended_events', related_name='attended_users', to='event.event'),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='going_events',
            field=models.ManyToManyField(db_table='user_going_events', related_name='going_users', to='event.event'),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='interested_events',
            field=models.ManyToManyField(db_table='user_interested_events', related_name='interested_users', to='event.event'),
        ),
    ]