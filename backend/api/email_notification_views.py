from email.errors import NonASCIILocalPartDefect
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models.event import Event
from event.models.non_registered import NonRegisteredUser
from .serializers import EventSerializer, NonRegisteredUserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from email_notification.emails import get_emails_from_users
from django.core.mail import BadHeaderError, send_mail, send_mass_mail
from django.http import HttpResponse, HttpResponseRedirect
from dotenv import load_dotenv

load_dotenv()
import os

@api_view(['GET'])
def get_non_registered_user_emails(request, id):
    try:
        event = Event.objects.get(id=id)
        non_registered_users = event.nonregistereduser_set.all()
        serializer = NonRegisteredUserSerializer(non_registered_users, many=True)
        print(get_emails_from_users(serializer.data))
        return Response(get_emails_from_users(serializer.data))
    except ObjectDoesNotExist:
        print("non registered users or event does not exist")

@api_view(['POST'])
def test_send_email(request):
    subject = request.POST.get('subject', 'test')
    message = request.POST.get('message', 'test')
    from_email = request.POST.get('from_email', 'testevent1337@gmail.com')
    print(subject, message, from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['testevent1337@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/api/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    


