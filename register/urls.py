__author__ = 'zeroonehacker'

from django.conf.urls import url
from register import views
from wkhtmltopdf.views import PDFTemplateView
urlpatterns  = [
    url(r'^$', views.register, name='register'),
    url(r'^loggedin/',views.loggedin, name='loggedin'),
    url(r'^registered/',views.registered, name='registered'),
    url(r'^change_password/', views.change_pass,name="change_pass"),
    url(r'^login/', views.login, name='login'),
    url(r'^form', views.registrationForm, name="Registration"),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^part_form/', views.forom, name="form"),
    url(r'^view_form/',views.view_form, name="view_form"),
    url(r'^pdf/$',views.generate_pdf,name='generate_pdf'),

    #url(r'^form/', views.forms, name='main_form'),
    #url(r'^login/', views.login, name='login'),
]
