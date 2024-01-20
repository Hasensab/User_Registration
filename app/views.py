from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    uo=User_form()
    po=Profile_form()
    d={'uo':uo,'po':po}
    if request.method=='POST' and request.FILES:
        UFO=User_form(request.POST)
        PFO=Profile_form(request.POST,request.FILES)
        if UFO.is_valid() and PFO.is_valid():
            MUFO=UFO.save(commit=False)
            pw=UFO.cleaned_data['password']
            MUFO.set_password(pw)
            MUFO.save()

            MPFO=PFO.save(commit=False)
            MPFO.username=MUFO
            MPFO.save()
            return HttpResponse('registration done successful')
        else:
            return HttpResponse('invalid data')

    return render(request,'registratio.html',d)
