from django.urls import path 
from .views import *

urlpatterns = [
    path("Create-Ride/",  CreateRide, name="CreateRide"),
    path("Request-Ride/", RideRequest_v, name="RequestRide"),
    path("Request-accept/",RequestAccept,name="RequestAccept"),
    path("Request-reject/",RequestReject,name="RequestReject"),
    path("Your-Ride/", Notification, name="YourRide"),
    path("Ride-stats/",CheckStatus, name="RideStatus"),
]