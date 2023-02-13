import uuid
from typing import List
from game_of_life.models import Game
from game_of_life.game import GameOfLife


def create_new_game() -> str:
    """ Создвет новую игру и возвращает ее уникальный код"""
    game = Game.objects.create(unique=uuid.uuid4(), alive_cells=[])
    game_of_life = GameOfLife.create_game(game)
    return game_of_life.game.unique


def get_game_of_life(unique: str) -> GameOfLife:
    """ Возвращает объект GameOfLife """
    return GameOfLife(Game.objects.get(unique=unique))


def take_next_step(unique: str) -> GameOfLife:
    """ Делает новый шаг в игре и возвращает объект Game измененное поле """
    game_of_life = get_game_of_life(unique)
    if not game_of_life.game.game_over:
        game_of_life.next_step()
    return game_of_life


def create_grid(game_of_life: GameOfLife) -> List[List[int]]:
    """ Возвращает игровое поле с 'живыми' клетками """
    return [[1 if [line, column] in game_of_life.game.alive_cells else 0
            for column in range(game_of_life.game.columns)]
            for line in range(game_of_life.game.lines)]


def get_params(game_of_life: GameOfLife) -> dict:
    """ Возвращает поле и состояние игры """
    return {
        'grid': create_grid(game_of_life),
        'game_over': game_of_life.game.game_over,
    }
