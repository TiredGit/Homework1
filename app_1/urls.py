from django.urls import path
from app_1.views import index, games, game1, game2

urlpatterns = [
    path('', index),
    path('games/', games),
    path('games/game1/', game1),
    path('games/game2/', game2)
]