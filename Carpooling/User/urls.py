from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("Registeration/",  UserRegister, name="register"),
    path('Add-Car/', AddCar, name='add_car'),
    path('Profile/',UserProfile, name='Profile'),
    re_path(r'search/',Search)
]
