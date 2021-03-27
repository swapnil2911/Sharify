from django.http import HttpResponse
from django.shortcuts import render
from Travels.models import Ride
from User.models import UserCar
from django.db.models import Q

def HomePage(request):
	print(request.body)
	if request.user.is_authenticated:
		driver = UserCar.objects.filter(driver = request.user)
		if driver.exists():
			ride = Ride.objects.filter(~Q(driver=driver[0]))
		else:	
			ride = Ride.objects.all()
		context = {'title' : 'Home', 'rides' : ride}
		return render(request,'User/Home.html',context)
	else:
		return render(request, 'User/Home.html')

def UserLogin(request):
	pass
