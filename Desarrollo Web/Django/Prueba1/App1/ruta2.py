#from django import url
from django.conf.urls import *
from django.urls import path
from django.contrib import admin

import views


urlpatterns = [
    path("",views.Vista2, name = "Vista2")
]