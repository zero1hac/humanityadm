__author__ = 'zeroonehacker'

from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
    di = {}
    di.update(csrf(request))
    return render(request,'login.html',di)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request,'loggedin.html',{'user':request.user.username})
    else:
        return render(request,'invalid.html',{})
def logout(request):
    auth.logout(request)
    return render(request,'logout.html',{})