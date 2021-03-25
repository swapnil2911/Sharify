from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
	context = {'title' : 'Home'}
	return render(request,'User/Home.html',context)

def UserLogin(request):
	pass