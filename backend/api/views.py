# Response object takes any python or serialized data and renders as JSON data
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models import Event, RegisteredUser, NonRegisteredUser
from .serializers import EventSerializer, NonRegisteredUserSerializer, RegisteredUserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import (get_list_or_404, HttpResponseRedirect)


@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    # many to true because serializing multiple items
    # one item make it false
    serializer = EventSerializer(events, many=True)
    # outputs as JSON data
    return Response(serializer.data)

@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
        print("invalid: ", serializer.errors)
    return Response(serializer.data)

# get event 
@api_view(['GET'])
def getEventByID(request, id):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        print("Event does not exist")

# delete event
@api_view(['DELETE'])
def deleteEvent(request, id):
    try:
        get_list_or_404(Event, id=id)
        Event.objects.filter(id=id).delete()
        return HttpResponseRedirect("/")
    except ObjectDoesNotExist:
        print("Event does not exist")


@api_view(['GET'])
def get_registered_users(request):
    registered_users = RegisteredUser.objects.all()
    serializers = RegisteredUserSerializer(registered_users, many=True)
    return Response(serializers.data)

# gets the non registered users connected to an event by event id
@api_view(['GET'])
def get_non_registered_users_by_event_id(request, id):
    try:
        event = Event.objects.get(id=id)
        non_registered_users = event.nonregistereduser_set.all()
        serializer = NonRegisteredUserSerializer(non_registered_users, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        print("non registered users or event does not exist")

@api_view(['GET'])
def get_non_registered_users(request):
    non_registered_users = NonRegisteredUser.objects.all()
    serializers = NonRegisteredUserSerializer(non_registered_users, many=True)
    return Response(serializers.data)

# adds a non registered user, must specify the event id
@api_view(['POST'])
def add_non_registered_user(request):
    serializer = NonRegisteredUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("invalid: ", serializer.errors)
    return Response(serializer.data)
