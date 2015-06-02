__author__ = 'zeroonehacker'

from django.conf.urls import url
from register import views
urlpatterns  = [
    url(r'^$', views.register, name='register'),
    url(r'^change_password/', views.change_pass,name="change_pass"),
    url(r'^login/', views.login, name='login'),
    url(r'^form/', views.registrationForm, name="Registration"),
    url(r'^logout/',views.logout,name='logout'),

    #url(r'^form/', views.forms, name='main_form'),
    #url(r'^login/', views.login, name='login'),
]
