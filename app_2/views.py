from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello! It's second app")

def countrys(request):
    return HttpResponse("Choose your country")

def country1(request):
    return HttpResponse("Russia")

def country2(request):
    return HttpResponse("Italy")