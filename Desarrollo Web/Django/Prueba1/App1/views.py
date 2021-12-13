from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Vista(request):
    return HttpResponse("Hola mundo xd")


def Vista2(request):
    return HttpResponse("Hello world xd")