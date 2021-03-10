from django.shortcuts import render, redirect
from .forms import CustUserCreationForm, CustUserChangeForm
from django.contrib.auth import login, authenticate

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
			return redirect('/')
	else:
		form = CustUserCreationForm()
	return render(request, 'User/Register.html', {'form':form})

def UserLogin(request):
	pass

def UserHistory(request):
	pass

def UserProfile(request):
	pass