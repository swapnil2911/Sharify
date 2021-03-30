from django.http import HttpResponse
from django.shortcuts import render
from Travels.models import Ride, RideRequest
from User.models import UserCar
from django.db.models import Q
from django.db import connection

def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def HomePage(request):
	print(request.body)
	if request.user.is_authenticated:
		cursor = connection.cursor()
		cursor.execute('SELECT ')
		# driver = UserCar.objects.filter(driver = request.user)
		# if driver.exists():
		# 	ride = Ride.objects.filter(~Q(driver=driver[0]))
		# else:	
		# 	ride = Ride.objects.all()
		# context = {'title' : 'Home', 'rides' : ride}
		rides = []
		user_requests = RideRequest.objects.filter(~Q(riderId = request.user)) 
		for user_request in user_requests:
			rides.append(user_request.rideId)
		context = {'title' : 'Home' , 'rides' : rides}
		return render(request,'User/Home.html',context)
	else:
		return render(request, 'User/Home.html')

def UserLogin(request):
	pass
