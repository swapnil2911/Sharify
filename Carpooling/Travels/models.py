from django.db import models
from User.models import User

# Create your models here.
class Travels(models.Model):
	StartingPoint     = models.CharField(max_length = 25)
	Passenger1        = models.ForeignKey(User, null = True, default = None, on_delete = models.CASCADE, related_name = 'Passenger1_type')
	Passenger2        = models.ForeignKey(User, null = True, default = None, on_delete = models.CASCADE, related_name = 'Passenger2_type')
	Passenger3        = models.ForeignKey(User, null = True, default = None, on_delete = models.CASCADE, related_name = 'Passenger3_type')
	Passenger4        = models.ForeignKey(User, null = True, default = None, on_delete = models.CASCADE, related_name = 'Passenger4_type')
	Driver            = models.ForeignKey(User, default = None, on_delete = models.CASCADE, related_name = 'Driver_type')
	EndingPoint       = models.CharField(max_length = 25, default = 1)
	Price             = models.IntegerField(default = 1)
	StartDate         = models.DateField()
	EndDate           = models.DateField()