from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index2(request):
    return HttpResponse("It's third app!!!.")

def test(request):
    return HttpResponse("Just a test")

def my_city(request):
    return HttpResponse("Ufa!")

