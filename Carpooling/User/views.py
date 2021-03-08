from django.shortcuts import render, redirect
from .forms import CustUserCreationForm, CustUserChangeForm

# Create your views here.
def UserRegister(request):
	if request.method == 'POST':
		form = CustUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
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