from django.urls import path 
from .views import *

urlpatterns = [
    path("Create-Ride/",  CreateRide, name="CreateRide"),
]