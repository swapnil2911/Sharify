from django.forms import ModelForm
from .models import Ride, RequestStatus, RideRequest

# def CreateRide()
class RideForm(ModelForm):
    
    class Meta:
        model = Ride 
        fields = ("startingPoint","endingPoint","price","startDate","endDate")
