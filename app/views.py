from django.shortcuts import render
from app.forms import *
# Create your views here.
def registration(request):
    uo=User_form()
    po=Profile_form()
    d={'uo':uo,'po':po}
    return render(request,'registratio.html',d)
