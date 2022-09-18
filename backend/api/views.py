# Response object takes any python or serialized data and renders as JSON data
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models import Event, RegisteredUser, NonRegisteredUser
from .serializers import EventSerializer, NonRegisteredUserSerializer, RegisteredUserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import (get_list_or_404, HttpResponseRedirect)


@api_view(['GET'])
def get_events():
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
        print("invalid: ", serializer.errors)
    return Response(serializer.data)


@api_view(['GET'])
def get_event_by_id(event_id):
    try:
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        print("Event does not exist")


@api_view(['DELETE'])
def delete_event(event_id):
    try:
        get_list_or_404(Event, id=event_id)
        Event.objects.filter(id=event_id).delete()
        return HttpResponseRedirect("/")
    except ObjectDoesNotExist:
        print("Event does not exist")


@api_view(['GET'])
def get_registered_users():
    registered_users = RegisteredUser.objects.all()
    serializers = RegisteredUserSerializer(registered_users, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_non_registered_users_by_event_id(event_id):
    try:
        event = Event.objects.get(id=event_id)
        non_registered_users = event.nonregistereduser_set.all()
        serializer = NonRegisteredUserSerializer(non_registered_users, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        print("non registered users or event does not exist")


@api_view(['GET'])
def get_non_registered_users():
    non_registered_users = NonRegisteredUser.objects.all()
    serializers = NonRegisteredUserSerializer(non_registered_users, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def add_non_registered_user(request):
    serializer = NonRegisteredUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("invalid: ", serializer.errors)
    return Response(serializer.data)
