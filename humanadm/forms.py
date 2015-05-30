from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=200)
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=("Male","Female"))
    nationality = forms.ChoiceField(choices=("GEN","OBC","SC","ST"))
    email = forms.EmailField()
