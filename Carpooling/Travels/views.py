from django.shortcuts import render
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
            driver = UserCar.objects.all(driver = request.user)
            instance.driver = driver
            instance.save()
    else:
        form = RideForm()
    return render(request, 'Ride/CreateRide.html',{'form' : form})