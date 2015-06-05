__author__ = 'zeroonehacker'
from django import forms
from django.contrib.auth.models import User
from .models import UserDetails

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','pattern':'.{8,}','title':'8 characters minimum','placeholder':'8 characters minimum'}),label="Password",help_text="Enter your Password",required=True)
    username = forms.CharField(widget=forms.HiddenInput(),label="Name",help_text="Enter Username",initial="lol")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="Email ID",help_text="Enter your Email")

    class Meta:
        model = User
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = UserDetails
        fields = ('full_name','father_name','mother_name','dob','gender','nation','category','phys','mobile','perma_addr','corres_addr')
class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'image'}))
    signature = forms.ImageField(widget=forms.FileInput(attrs={'id':'image'}))
    score_card = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = UserDetails
        fields = ('image','signature','score_card')