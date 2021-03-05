from django.db import models

# Create your models here.
class Car(models.Model):
	Brand           = models.CharField(max_length = 27)
	MaxSeating      = models.IntegerField()
	LicenseNumber   = models.CharField(max_length = 27)
	YearsUsed       = models.IntegerField()
	Mileage         = models.IntegerField()


class User(models.Model):
	username        = models.CharField(unique = True,max_length = 10, null = True)
	FirstName       = models.CharField(max_length = 27, null = True)
	LastName       	= models.CharField(max_length = 27, null = True)
	Email           = models.EmailField()
	MobileNumber    = models.IntegerField()
	Car             = models.ForeignKey(Car, null = True, on_delete = models.CASCADE, unique = True)
