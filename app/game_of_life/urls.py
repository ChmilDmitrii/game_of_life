from django.urls import path
from game_of_life.views import create_game
from game_of_life.views import GameNextStep

urlpatterns = [
    path('', create_game, name='create_game'),
    path('game/<str:unique>', GameNextStep.as_view(), name='game_next_step')
]
