from django.forms import ModelForm
from .models import Ride, RequestStatus, RideRequest
from django import forms

# def CreateRide()
class RideForm(ModelForm):
    
    class Meta:
        model = Ride 
        fields = ("startingPoint","endingPoint","price","startDate","endDate")
        widgets = {
        	'startDate': forms.SelectDateWidget(),
            'endDate': forms.SelectDateWidget(),
    	}
        labels = {
            'startingPoint': "Source",
            'endingPoint': "Destination",
            'startDate': "Journey Start Date",
            'endDate': "Journey End date",
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")

class RequestForm(ModelForm):

    class Meta:
        model = RideRequest
        fields = ('rideId',)