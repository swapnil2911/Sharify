from django.db import models
from django.utils import timezone
from User.models import User,UserCar

# Create your models here.
class Ride(models.Model):
	startingPoint     = models.CharField(max_length = 25)
	driver            = models.ForeignKey(UserCar, default = None, on_delete = models.CASCADE, related_name = 'Driver_type')
	endingPoint       = models.CharField(max_length = 25, default = 1)
	price             = models.IntegerField(default = 1)
	createdOn         = models.DateField(default = timezone.now)
	startDate         = models.DateField()
	endDate           = models.DateField()

	def concat(self):
		details = self.startingPoint + "-" + self.endingPoint
		return details
		

	def __str__(self):
		return self.concat()
	

class RequestStatus(models.Model):
	description       = models.CharField(max_length = 27)
	def __str__(self):
		return self.description
	

class RideRequest(models.Model):
	riderId           = models.ForeignKey(User, on_delete = models.CASCADE)
	rideId            = models.ForeignKey(Ride, on_delete = models.CASCADE)
	createdOn         = models.DateField(default = timezone.now)
	requestStatusID   = models.ForeignKey(RequestStatus, on_delete = models.CASCADE)

	def __str__(self):
		return self.riderId.userName + "-" + self.rideId.concat()
	

	
