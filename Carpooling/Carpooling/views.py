from django.http import HttpResponse

def HomePage(request):
	return HttpResponse('<h1>This is the homepage</h1>')

def UserHistory(request):
	pass

def UserProfile(request):
	pass

def AvailableTravel(request):
	pass

def MakeTravel(request):
	pass
