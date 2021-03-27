from django.urls import path 
from .views import *

urlpatterns = [
    path("Create-Ride/",  CreateRide, name="CreateRide"),
    path("Request-Ride/", RideRequest_v, name="RequestRide"),
    path("Your-Ride/", Notification, name="YourRide"),
]