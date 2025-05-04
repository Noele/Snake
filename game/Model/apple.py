from random import randrange

from config.colours import Colours
from game.Model.player import Player
from config.settings import Settings


class Apple:
    def __init__(self, settings: Settings, player: Player):
        self.position: tuple[int, int] = (0, 0)
        self.map_size: tuple[int, int] = settings.game_size
        self.settings: Settings = settings
        self._spawn(player.tail_position)

    def _spawn(self, tail: list[tuple[int, int]]) -> None:
        self.position = (randrange(1, self.map_size[0] - 1), randrange(1, self.map_size[1] - 1))
        if self.position in tail:
            self._spawn(tail)

    def update(self, player: Player) -> None:
        if player.position == self.position:
            player.grow()
            self._spawn(player.tail_position)

    def draw(self, map: list[list[str]]) -> None:
        map[self.position[1]][self.position[0]] = f"{self.settings.apple_colour}●{Colours.RESET}"

