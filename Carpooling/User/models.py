from django.db import models

# Create your models here.
class Car(models.Model):
	name 			= models.CharField(max_length = 27, null = True, unique = True)	
	model           = models.CharField(max_length = 27)
	make            = models.CharField(max_length = 27, null = True)
	makeYear		= models.DateField()
	def __str__(self):
		return self.name
	


class User(models.Model):
	userName        = models.CharField(unique = True, max_length = 10, null = True)
	firstName       = models.CharField(max_length = 27, null = True)
	lastName       	= models.CharField(max_length = 27, null = True)
	email           = models.EmailField()
	mobileNumber    = models.IntegerField()
	driverLicense	= models.CharField(null = True, max_length = 27, unique = True)
	licenseValidFrom = models.DateField(null = True)
	def __str__(self):
		return self.userName
	
	
class UserCar(models.Model):
	driver           = models.ForeignKey(User, on_delete = models.CASCADE)
	car 			 = models.ForeignKey(Car, on_delete = models.CASCADE)
	carColor		 = models.CharField(max_length = 27)
	carRegisteration = models.CharField(max_length = 27)
	
