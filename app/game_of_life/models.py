from django.db import models


class Game(models.Model):
    unique = models.UUIDField('Unique code', unique=True)
    lines = models.PositiveIntegerField(
        'Number of lines on the grid',
        default=50,
    )
    columns = models.PositiveIntegerField(
        'Number of columns on the grid',
        default=50,
    )
    alive_cells = models.JSONField('Alive cells')
    game_over = models.BooleanField('Game over', default=False)

    def __str__(self):
        return f"Game {self.pk}"
