from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.template import loader, RequestContext
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lgin
from django.shortcuts import render,redirect
from django.contrib.auth import logout as lgout
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.core.mail import send_mail
from .forms import UserForm, UserProfileForm
from .models import UserDetails,User
import smtplib
import string
import random
# Create your views here.
class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
	
    def send_message(self, receivers,subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            receivers,
            headers + "\r\n\r\n" + body)

def register(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                t= UserDetails(user=user,email=request.POST['email'])
                t.save()
                #profile = profile_form.save(commit=False)
                #profile.user = user
                #profile.save()
                registered = True
                return render(request,'register/login.html',{'message':'You are successfully registered! LogIn'})
            else:
                print user_form.errors,
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()
        return render(request,'register/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered},context)
    else:
        return HttpResponse("You are already Logged In! <a href='/register/form/'>Click Here</a> to fill the form")
def change_pass(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            return HttpResponse("Email Id is not registered")
        gmail = Gmail('','')#email password please
        passcode = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
        gmail.send_message(email,"Change Password IIT PORTAL","Your new password is "+passcode)
        user.set_password(passcode)
        user.save()
        return HttpResponse("You new password is sent to your registered Email ID")
    else:
        return render(request,'register/change_pass.html',{})
def login(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
                username = request.POST['username']
                try:
                    user = User.objects.get(username=username)
                except:
                    return HttpResponse("User doesn't exist")
                passcode = request.POST['password']
                if user.check_password(passcode):
                    user = authenticate(username=username,password=passcode)
                    lgin(request,user)
                    return HttpResponseRedirect('/register/form/')
                else:
                    return HttpResponse("Wrong password")
        else:
            return render(request,'register/login.html',{})
    else:
        return HttpResponseRedirect('/register/form/')
def registrationForm(request):
    if request.user.is_authenticated():
        if request.method == 'POST':

            user_name = UserDetails.objects.get(user=request.user)

            #return HttpResponse("Something went wrong")
            if 'save' in request.POST:
                user_name.full_name = request.POST['full_name']
                user_name.father_name = request.POST['father_name']
                user_name.mother_name = request.POST['mother_name']
                user_name.dob = request.POST['dob']
                user_name.gender = request.POST['gender']
                user_name.nation = request.POST['nation']
                user_name.category = request.POST['category']
                user_name.phys = request.POST['phys']
                user_name.mobile = request.POST['mobile']
                user_name.perma_addr = request.POST['perma_addr']
                user_name.corres_addr = request.POST['corres_addr']
                user_name.save()
                return HttpResponse("form submitted")
            if 'submit' in request.POST:
                user_name.full_name = request.POST['full_name']
                user_name.father_name = request.POST['father_name']
                user_name.mother_name = request.POST['mother_name']
                user_name.dob = request.POST['dob']
                user_name.gender = request.POST['gender']
                user_name.nation = request.POST['nation']
                user_name.category = request.POST['category']
                user_name.phys = request.POST['phys']
                user_name.mobile = request.POST['mobile']
                user_name.perma_addr = request.POST['perma_addr']
                user_name.corres_addr = request.POST['corres_addr']
                user_name.submitt = "Y"
                user_name.save()
                return HttpResponse("FormSubmitted")
        else:
            return render(request,'registration.html',{})
    else:
        return HttpResponseRedirect('/register/login/')
@login_required(login_url='/register/login')
def logout(request):
    lgout(request)
    return render(request,'register/login.html',{'message':'You are logged out Successfully ....Enter below to login again'})
