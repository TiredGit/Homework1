from django.urls import path
from app_2.views import *

urlpatterns = [
    path('index/', index),
    path('index/countrys', countrys),
    path('index/countrys/country1', country1),
    path('index/countrys/country2', country2),
]