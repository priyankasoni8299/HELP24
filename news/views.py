from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import News,Newsinfo
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True)
def main(request):
	#print(request.session)
	if request.session.get('loginstatus', None)!="1":
		return redirect('../relogin/')
def index (request):
    return render(request, 'login.html')
def Newstype(request,pk):
	if('loginstatus' not in request.session):
		return redirect('../../relogin/')
	else:
		data=Newsinfo.objects.filter(News=pk)
		context={
		    "d":data
		}
		return render(request,'breakingnewsdata.html',context)
def newsuser(request):
	#fetch all news from modal
	if('loginstatus' not in request.session):
		return redirect('../../relogin/')
	else:
		data=News.objects.all().order_by('news_type')
		context={
			"d":data
		}
		return render(request,'newsuser.html',context)
def breakingnewsdata(request, pk):
	if('loginstatus' not in request.session):
		return redirect('../../../relogin/')
	else:
		data=Newsinfo.objects.filter(city__iexact=request.session['mycity'])
		data=data.filter(news=pk);
		print(data.query)
		context={
			"d":data
		}
		return render(request,'breakingnewsdata.html', context)