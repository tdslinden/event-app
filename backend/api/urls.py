from django.urls import path
from . import views
from . import email_notification_views

urlpatterns = [
    path('add/event/', views.addEvent),
    path('delete/<int:id>/', views.deleteEvent),
    path('get/<int:id>/', views.getEventByID),
    path('', views.getEvents),
    path('get/non-registered-users/<int:id>/', views.get_non_registered_users_by_event_id),
    path('add/non-registered-user/', views.add_non_registered_user),
    path('get/non-registered-users/', views.get_non_registered_users),
    path('get/non-registered-users/emails/<int:id>/', email_notification_views.get_non_registered_user_emails),
    path('send/test-email/', email_notification_views.test_send_email)
]