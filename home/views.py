from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
# Create your views here
def main(request):
	#print(request.session)
	if request.session.get('loginstatus', None)!="1":
		return redirect('../relogin/')
	if('mycity' in request.POST):
		request.session['mycity'] = request.POST['mycity']
	else:
		print(request.session)
		if(request.session.get('mycity', None)==None):
			request.session['mycity'] = "indore"
	#print(request.session['mycity'])
	#print(request.session['loginstatus'])
	#print(request.session['loginpk'])
	return render(request,'home1.html', {"sess" : request.session['mycity']})