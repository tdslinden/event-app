# Generated by Django 4.0.4 on 2022-07-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonRegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
            ],
        ),
    ]
