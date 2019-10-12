from django.shortcuts import render, redirect
from django.http import HttpResponse
from directory.models import Categories, Directory_info
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True)
def main(request):
	#print(request.session)
	if request.session.get('loginstatus', None)!="1":
		return redirect('../relogin/')
def index (request):
    return redirect('../')
def directory (request):
	if('loginstatus' not in request.session):
		return redirect('../../relogin/')
		#return render(request, 'login.html')
	data=Categories.objects.all().order_by('category_name')
	context={
	    "d":data
	}
	return render(request, 'directory.html',context)
def directoryinfo (request, pk):
	if('loginstatus' not in request.session):
		return redirect('../../../relogin/')
		#return render(request, 'login.html')
	data=Directory_info.objects.filter(city__iexact=request.session['mycity'])
	data=data.filter(category=pk)
	context={
	    "d":data,
	}
	return render(request, 'directoryinfo.html',context)