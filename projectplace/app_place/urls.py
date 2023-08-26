from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from app_place import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student',views.student, name='student'),
    path('recruiter',views.recruiter, name='recruiter'),
    path("about", views.about, name='about'),
    path("contactus", views.contactus, name='contactus'),
    path("stdlogin",views.stdLogin, name='stdlogin'),
    path("stdregister",views.stdRegister, name='stdregister'),
    path("recregister",views.recRegister, name='recregister'),
    path("reclogin",views.recLogin, name='reclogin'),
    path("logout", views.logoutUser, name='logout'),
]
