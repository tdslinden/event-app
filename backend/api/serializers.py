from rest_framework import serializers
# from event.models.event import Event
from event.models.non_registered import NonRegisteredUser
from event.models import RegisteredUser, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class NonRegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonRegisteredUser
        fields = '__all__'


class RegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = '__all__'
