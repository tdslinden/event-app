from django.urls import path
from . import views

urlpatterns = [
    path('add/event', views.addEvent),
    path('delete/<int:id>/', views.deleteEvent),
    path('get/<int:id>/', views.getEventByID),
    path('', views.getEvents),
    path('add/non-registered-user', views.add_non_registered_user),
    path('get/non-registered-users', views.get_non_registered_users)
]