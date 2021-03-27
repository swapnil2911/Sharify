from django.shortcuts import render, redirect
from .forms import CustUserCreationForm, CustUserChangeForm, UserCarForm
from django.contrib.auth import login, authenticate
from .models import UserCar
from Travels.models import Ride
from django.db.models import Q
# Create your views here.
def UserRegister(request):
	if request.method == 'POST':
		form = CustUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.userName, password=raw_password)
			login(request, user)
			if user.driverLicense is not None or user.licenseValidFrom is not None:
				print('Has drivers license')
				return redirect('/user/Add-Car')
			return redirect('/')
	else:
		form = CustUserCreationForm()
	return render(request, 'User/Register.html', {'form':form})

def UserLogin(request):
	pass

def AddCar(request):
	driver = request.user
	if driver.driverLicense is None or driver.licenseValidFrom is None:
		return redirect('/')
	if request.method == 'POST':
		form = UserCarForm(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.driver = driver
			instance.save()
			return redirect('/')
	else:
		form = UserCarForm()
	
	return render(request, 'User/Driver.html', {'form' : form})

def UserHistory(request):
	pass

def UserRide(request):
	user = request.user
	driver = UserCar.objects.filter(driver=user)[0]
	rides = Ride.objects.filter(driver=driver)
	return render(request, 'Travels/Notification.html', {'rides': rides})

def UserProfile(request):
	user = request.user
	driver = UserCar.objects.filter(driver=user)
	if driver.exists():
		ride = Ride.objects.filter(driver=driver[0])
	else:	
		return render(request,'User/Profile.html', {'user' : user})
	return render(request,'User/Profile.html',{'user':user, 'rides' : ride})

def Search(request):
	if request.method=='GET':
		q = request.GET.get('q')
		driver = UserCar.objects.filter(driver = request.user)[0]
		posts = Ride.objects.filter(startingPoint__icontains=q).exclude(driver=driver)
		return render(request, 'User/Home.html',{'posts': posts, 'query': q})
	else:
		return HttpResponse('Please submit a search term.')
