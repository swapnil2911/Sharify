from django.db import models

# Create your models here.
class User(models.Model):
	FirstName       = models.CharField(max_length = 27)
	LastName       	= models.CharField(max_length = 27)
	Email           = models.EmailField()
	MobileNumber    = models.IntegerField()
	Car             = models.CharField(max_length = 27, null = True)
