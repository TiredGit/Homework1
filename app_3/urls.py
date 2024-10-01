from django.urls import path
from app_3.views import *

urlpatterns = [
    path('index2/', index2),
    path('index2/test', test),
    path('my_city/', my_city)
]