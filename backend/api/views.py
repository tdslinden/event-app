# Response object takes any python or serialized data and renders as JSON data
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models import Event
from .serializers import EventSerializer
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
    
    