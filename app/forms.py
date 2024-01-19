from django import forms
from app.models import *

class User_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        helptext={'username':''}
class Profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['addr','pro_pic']