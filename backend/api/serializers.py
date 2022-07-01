from dataclasses import fields
from rest_framework import serializers
from event.models.event import Event
from event.models.event import NonRegisteredUser

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class NonRegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonRegisteredUser
        fields = '__all__'