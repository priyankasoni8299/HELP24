from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import user
from . models import *

from django.contrib.auth import authenticate,login
from django.forms import ModelForm

class loginForm(ModelForm):
	class Meta:
		model = Login
		fields = ['firstname', 'lastname','email', 'password']

def index (request):
	if request.method=="POST":
		if('signin' in request.POST):
			#request from login from
			email= request.POST['email']
			password= request.POST['password']
			obj = Login.objects.filter(email = email)
			num_results = obj.count()
			print("username count = ", num_results)
			if(num_results>=1):		#valid user name
				obj1 = obj.filter(password=password)
				print(obj1)
				num_results = obj1.count()
				print("password count = ", num_results)
				if(num_results==1):		#valid password
					request.session['loginstatus']="1"
					tmp = obj1.get(email=email)
					request.session['loginpk']=tmp.id
					return redirect('/home/')
				else:
					msg = {"errorMsg":"2"}
					return render(request, 'login.html', msg)
			else:
				msg = {"errorMsg":"1"}
				return render(request, 'login.html', msg)
		else:
			if('mycity' in request.POST):
				return redirect('/home/')
			else:
				#request from signup form
				firstname= request.POST['firstname']
				lastname= request.POST['lastname']
				email= request.POST['email']
				password= request.POST['password']
				cpassword= request.POST['cpassword']
				if(password==cpassword):
					frm = loginForm(request.POST or none)
					frm.save()
					return render(request,"login.html")
				else:
					pass
	return render(request,"login.html")

def logout(request):
	auth.logout(request)
	return render(request,"login.html")
    #return render(request, 'login.html')



# Create your views here.
