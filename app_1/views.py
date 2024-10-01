from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. My name is Eduard")

def games(request):
    return HttpResponse("Choose your game")

def game1(request):
    return HttpResponse("It's CS")

def game2(request):
    return HttpResponse("It's Dota")