from django import forms
from django.contrib.auth.models import User
from . import models
import re


class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['bloodgroup','address','mobile','profile_pic']
    
    def clean_mobile(self):
        mobile_no=self.cleaned_data.get('mobile')
        # regex = "^\\+?[1-9][0-9]{7,14}$"
        regex = re.compile("(0|91)?[7-9][0-9]{9}")
        if not regex.match(mobile_no):
            raise forms.ValidationError('Invalid Mobile Number....')
        return mobile_no


class DonationForm(forms.ModelForm):
    class Meta:
        model=models.BloodDonate
        fields=['age','bloodgroup','disease','unit']

