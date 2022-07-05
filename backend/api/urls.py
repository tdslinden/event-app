from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addEvent),
    path('delete/<int:id>/', views.deleteEvent),
    path('get/<int:id>/', views.getEventByID),
    path('', views.getEvents),
    path('users/', views.get_all_users),
]