from typing import List, Generator
from random import randint
from game_of_life.models import Game


class Cell:

    def __init__(self, line: int, column: int) -> None:
        self.line = line
        self.column = column

    def get_list(self) -> List[int]:
        """ Возвращает координаты клетки """
        return [self.line, self.column]


class GameOfLife:

    def __init__(self, game: Game) -> None:
        self.game = game

    @classmethod
    def create_game(cls, game: Game):
        """ Возвращает экземпляр класса с созданным игровым полем """
        game_of_life = cls(game)
        game_of_life.create_alive_cells()
        return game_of_life

    def grid(self) -> Generator[Cell, None, None]:
        """
        Возвращает объект генератор, который
        позволяет перебрать все клетки на поле
        """
        for line in range(self.game.lines):
            for column in range(self.game.columns):
                yield Cell(line, column)

    def create_alive_cells(self) -> None:
        """ Создает живые клетки """
        for cell in self.grid():
            if randint(0, 1):
                self.game.alive_cells.append(cell.get_list())
        self.game.save()

    def get_alive_neighbors(self, cell: Cell) -> int:
        """ Возвращает количество 'живых' соседей вокруг клетки """
        alive_neighbors = 0
        for n_line in range(-1, 2):
            for n_column in range(-1, 2):
                if n_line == 0 and n_column == 0:
                    continue
                if [(cell.line + n_line) % self.game.lines,
                        (cell.column + n_column) % self.game.columns] \
                        in self.game.alive_cells:
                    alive_neighbors += 1
        return alive_neighbors

    @staticmethod
    def update_state_cell(alive: bool, alive_neighbors: int) -> bool:
        """
        Возвращает новое состояние клетки
        в соответствии с условиями игры
        """
        if alive:
            if alive_neighbors == 2 or alive_neighbors == 3:
                return True
            return False
        if alive_neighbors == 3:
            return True
        return False

    def check_new_step(self, new_alive_cells: List[List[int]]) -> bool:
        """ Проверяет новый шаг на условия окончания игры """
        if len(new_alive_cells) == 0:
            self.game.game_over = True
            return False
        if self.game.alive_cells == new_alive_cells:
            self.game.game_over = True
            return False
        return True

    def next_step(self) -> None:
        """ Делает новый шаг в игре """
        new_alive_cells = []
        for cell in self.grid():
            alive = True if cell.get_list() in self.game.alive_cells \
                else False
            alive_neighbors = self.get_alive_neighbors(cell)
            if self.update_state_cell(alive, alive_neighbors):
                new_alive_cells.append(cell.get_list())
        if self.check_new_step(new_alive_cells):
            self.game.alive_cells = new_alive_cells
        self.game.save()
