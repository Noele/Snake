from random import randrange

from config.Colours import Colours
from game.Model.Player import Player
from config.Settings import Settings


class Apple:
    def __init__(self, settings: Settings):
        self.position: tuple[int, int] = (0, 0)
        self.map_size: tuple[int, int] = settings.game_size
        self.settings: Settings = settings
        self._spawn()

    def _spawn(self) -> None:
        self.position = (randrange(1, self.map_size[0] - 1), randrange(1, self.map_size[1] - 1))

    def update(self, player: Player) -> None:
        if player.position == self.position:
            player.grow()
            self._spawn()

    def draw(self, map: list[list[str]]) -> None:
        map[self.position[1]][self.position[0]] = f"{self.settings.apple_colour}a{Colours.RESET}"

