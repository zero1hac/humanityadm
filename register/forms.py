__author__ = 'zeroonehacker'
from django import forms
from django.contrib.auth.models import User
from .models import UserDetails

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="Password",help_text="Enter your Password")
    username = forms.CharField(widget=forms.TextInput(),label="Username",help_text="Enter Username")
    email = forms.EmailField(widget=forms.EmailInput(),label="Email ID",help_text="Enter your Email")

    class Meta:
        model = User
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = UserDetails
        fields = ('full_name','father_name','mother_name','dob','gender','nation','category','phys','mobile','perma_addr','corres_addr')