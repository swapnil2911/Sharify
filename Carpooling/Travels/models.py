from django.db import models
from User.models import User

# Create your models here.
class Ride(models.Model):
	StartingPoint     = models.CharField(max_length = 25)
	Driver            = models.ForeignKey(User, default = None, on_delete = models.CASCADE, related_name = 'Driver_type')
	EndingPoint       = models.CharField(max_length = 25, default = 1)
	Price             = models.IntegerField(default = 1)
	StartDate         = models.DateField()
	EndDate           = models.DateField()

