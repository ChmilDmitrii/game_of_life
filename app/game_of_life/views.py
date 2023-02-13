from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View

from game_of_life.utils import create_new_game
from game_of_life.utils import get_game_of_life
from game_of_life.utils import take_next_step
from game_of_life.utils import get_params
from game_of_life.errors import errors_handler


def create_game(request):
    """ Создает игру и редиректит на /game/<str:unique> """
    unique = create_new_game()
    return redirect(reverse(
        'game_next_step',
        args=(unique,),
    ))


class GameNextStep(View):

    @staticmethod
    @errors_handler
    def get(request, unique):
        """ Возвращает текущее состояние поля"""
        game_of_life = get_game_of_life(unique)
        return render(request, 'game.html', get_params(game_of_life))

    @staticmethod
    @errors_handler
    def post(request, unique):
        """ Делает шаг и возвращает новое состояние поля"""
        game_of_life = take_next_step(unique)
        return render(request, 'game.html', get_params(game_of_life))
