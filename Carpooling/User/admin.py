from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Car, UserCar
from .forms import CustUserChangeForm, CustUserCreationForm

# Register your models here.

class CustUserAdmin(UserAdmin):
	form = CustUserChangeForm
	add_form = CustUserCreationForm

	list_display = ('userName', 'email', 'firstName', 'lastName', 'mobileNumber',)
	list_filter = ('is_admin',)

	fieldsets = (
        (None, {'fields': ('userName', 'password')}),
        ('Personal info', {'fields': ('email','mobileNumber','firstName','lastName','driverLicense','licenseValidFrom',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

	add_fieldsets = (
       	(None, {
            'classes': ('wide',),
            'fields': ('email', 'userName', 'firstName', 'lastName', 'mobileNumber','driverLicense','licenseValidFrom', 'password1', 'password2'),
        }),
    )


	search_fields = ('userName', 'email', 'firstName','lastName', 'mobileNumber',)
	ordering      = ('userName', 'email', 'firstName','lastName', 'mobileNumber',)
	filter_horizontal = ()


admin.site.register(User, CustUserAdmin)
admin.site.register(Car)
admin.site.register(UserCar)