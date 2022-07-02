# Response object takes any python or serialized data and renders as JSON data
from email.errors import NonASCIILocalPartDefect
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models.event import Event
from event.models.non_registered import NonRegisteredUser
from .serializers import EventSerializer, NonRegisteredUserSerializer
from django.core.exceptions import ObjectDoesNotExist

# from backend.api import serializers

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
        Event.objects.filter(id=id).delete()
    except ObjectDoesNotExist:
        print("Event does not exist")

# gets the non registered users by event id
@api_view(['GET'])
def get_non_registered_users_by_event_id(request, id):
    try:
        event = Event.objects.get(id=id)
        non_registered_users = event.nonregistereduser_set.all()
        serializer = NonRegisteredUserSerializer(non_registered_users, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        print("No non registered users")

@api_view(['GET'])
def get_non_registered_users(request):
    non_registered_users = NonRegisteredUser.objects.all()
    serializers = NonRegisteredUserSerializer(non_registered_users, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def add_non_registered_user(request):
    serializer = NonRegisteredUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
        print("invalid: ", serializer.errors)
    return Response(serializer.data)
