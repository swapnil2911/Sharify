from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class Car(models.Model):
	name 			= models.CharField(max_length = 27, null = True, unique = True)	
	model           = models.CharField(max_length = 27)
	make            = models.CharField(max_length = 27, null = True)
	makeYear		= models.DateField()
	def __str__(self):
		return self.name
	
class CustUserManager(BaseUserManager):
	def create_user(self, userName, email, firstName, mobileNumber, password = None):
		if not userName:
			raise ValueError('User must have username')

		if not email:
			raise ValueError('User must have email')

		user = self.model(userName = userName, email = self.normalize_email(email), firstName = firstName, mobileNumber = mobileNumber,)

		user.set_password(password)
		user.save(using = self._db)

		return user

	def create_superuser(self, userName, email, firstName, mobileNumber, password = None):
		user = self.create_user(userName, email, firstName, mobileNumber, password)
		
		user.is_admin = True
		user.save(using = self._db)

		return user

class User(AbstractBaseUser):
	userName         = models.CharField(verbose_name = 'Username', max_length = 27, unique = True)
	email            = models.CharField(verbose_name = 'Email Address', max_length = 27, unique = True)
	firstName        = models.CharField(verbose_name = 'First Name',max_length = 27)
	lastName         = models.CharField(verbose_name = 'Last Name' ,max_length = 27, null = True)
	mobileNumber     = models.CharField(verbose_name = 'Mobile Number',max_length = 27 ,unique = True)
	driverLicense	 = models.CharField(verbose_name = 'Driver License', null = True, max_length = 27, unique = True,blank = True)
	licenseValidFrom = models.DateField(verbose_name = 'License Validity Date', null = True, blank = True)
	is_active        = models.BooleanField(default = True)
	is_admin         = models.BooleanField(default = False)

	objects = CustUserManager()

	USERNAME_FIELD  = 'userName'
	REQUIRED_FIELDS = ['email', 'firstName', 'mobileNumber', ]

	def __str__(self):
		return self.userName

	def has_perm(self, perm, obj = None):
		return True

	def has_module_perms(self,app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin
	
	
	
class UserCar(models.Model):
	driver           = models.ForeignKey(User, on_delete = models.CASCADE)
	car 			 = models.ForeignKey(Car, on_delete = models.CASCADE)
	carColor		 = models.CharField(max_length = 27)
	carRegisteration = models.CharField(max_length = 27)
	
	def __str__(self):
		return self.driver.userName
	
