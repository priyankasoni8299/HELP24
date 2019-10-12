from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import user
from . models import *


# Create your views here.
def index(request):
	request.session.flush()
	print('logout')
	return render(request, 'login.html')