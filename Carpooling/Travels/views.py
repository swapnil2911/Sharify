from django.shortcuts import render, redirect
from django.http import request
from .forms import RideForm
from .models import Ride, RequestStatus, RideRequest
from User.models import User, UserCar
# Create your views here.
def CreateRide(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            # driver = UserCar.objects.raw(f"SELECT * FROM user_usercar WHERE driver_id IN (SELECT id FROM user_user WHERE userName = {request.user})")
            driver = UserCar.objects.filter(driver = request.user)
            print(driver)
            if not driver.exists():
                return redirect('/')
            instance.driver = driver[0]
            instance.save()
    else:
        form = RideForm()
    return render(request, 'Travels/CreateRide.html',{'form' : form})

def RideRequest(request):
    pass