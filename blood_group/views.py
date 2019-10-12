from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import ModelForm
from blood_group.models import Blood
from django.views.decorators.cache import cache_control

class DonnerForm(ModelForm):
    class Meta:
        model = Blood
        fields = ['Name', 'bloodgrouptype', 'Age','Contact','Email', 'city']

    
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True)
def main(request):
    #print(request.session)
    if request.session.get('loginstatus', None)!="1":
        return redirect('../relogin/')
def index (request):
    if('loginstatus' not in request.session):
       return redirect('../../relogin/')
    else:    
        return render(request, 'bloodbank.html')

def bloodbank (request):
    if('loginstatus' not in request.session):
       return redirect('../../../relogin/')
    else:
        return render(request, 'bloodbank.html')

def donarinfo (request):
    if('loginstatus' not in request.session):
       return redirect('../../relogin/')
    else:
        return render(request, 'donarinfo.html')

def donarregistration (request, template_name='donarregistration.html'):
    if('loginstatus' not in request.session):
        return redirect('../../relogin/')
    else:
        form = DonnerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, template_name, {'form':form})
        #return render(request, 'donarregistration.html')


def donorsearch (request):
    if('loginstatus' not in request.session):
        return redirect('../../relogin/')
    else:
        try:
            tmp_bg = request.GET.get('bg', None)
        except NameError:
            pass
        else:
            pass
        if(tmp_bg==None):
            return render(request, 'donorsearch.html')
        else:
            data = {"bg":tmp_bg}
            switcher = {
                "aplus": "A+",
                "aminus": "A-",
                "bplus": "B+",
                "bminus": "B-",
                "abplus": "AB+",
                "abminus": "AB-",
                "oplus": "O+",
                "ominus": "O-",
            }
            tmp_bg = switcher.get(tmp_bg, "none")
            data=Blood.objects.filter(city__iexact=request.session['mycity'])
            b=data.filter(bloodgrouptype=tmp_bg)
            #print(b)
            return render(request, 'donarinfo.html',{"b":b})


# Create your views here.