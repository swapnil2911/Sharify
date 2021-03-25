from django.urls import path 
from .views import *

urlpatterns = [
    path("Registeration/",  UserRegister, name="register"),
]
