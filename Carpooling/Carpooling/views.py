from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
	context = {'title' : 'Home'}
	return render(request,'Home.html',context)

def UserHistory(request):
	pass

def UserProfile(request):
	pass

def AvailableTravel(request):
	pass

def MakeTravel(request):
	pass

def UserLogin(request):
	pass