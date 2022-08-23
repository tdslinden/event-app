from django.db import models


class EventImage(models.Model):
    title = models.CharField(max_length=255)
    image_link = models.ImageField(upload_to='media/')
