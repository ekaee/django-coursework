from django.shortcuts import render
from django.http import HttpResponse

def index(requrest):
    return HttpResponse("Rango says hey there partner!")