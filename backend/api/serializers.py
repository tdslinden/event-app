from dataclasses import fields
from rest_framework import serializers
from event.models.event import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
