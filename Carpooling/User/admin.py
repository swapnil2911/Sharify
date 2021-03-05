from django.contrib import admin
from .models import User, Car, UserCar
# Register your models here.
admin.site.register(User)
admin.site.register(Car)
admin.site.register(UserCar)