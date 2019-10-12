from django.shortcuts import render, redirect
from django.http import HttpResponse
from job_vecancy.models import Fields,Vacancyinfo
from django.views.decorators.cache import cache_control

# Create your views here.s
@cache_control(no_cache=True, must_revalidate=True)
def main(request):
    #print(request.session)
    if request.session.get('loginstatus', None)!="1":
        return redirect('../relogin/')
def vacancyinfo(request,pk):
    if('loginstatus' not in request.session):
       return redirect('../../../relogin/')
    else:
        data= Vacancyinfo.objects.filter(city__iexact=request.session['mycity'])
        data=data.filter(fields=pk)
        context={
        "a":data
        }
        return render(request, 'vacancyinfo.html',context)
def vacancy(request):
    data=Fields.objects.all().order_by('field_name')
    context={
      "a":data
    }
    if('loginstatus' not in request.session):
       return redirect('../../relogin/')
    else:    
        return render(request, 'vacancy.html',context)

def About(request):
    if('loginstatus' not in request.session):
        return redirect('../../relogin/')
    else:    
        return render(request, 'About.html')
def feedback1(request):
    if('loginstatus' not in request.session):
        return redirect('../../relogin/')
    else:
        return render(request, 'feedback1.html')
def help1(request):
    if('loginstatus' not in request.session):
        return redirect('../../relogin/')
    else:    
        return render(request, 'help1.html')


# Create your views here.
