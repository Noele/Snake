from keyboard import KeyboardEvent

from game.Model.Apple import Apple
from game.Model.Player import Player
from menu.Menu import MenuType

from menu.Menu import Menu

from config.Settings import Settings


class Game(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)

        self.size = self.settings.game_size
        self.map: list[list[str]] = self.initialize_map()
        self.player: Player = Player(self.settings)
        self.apple: Apple = Apple(self.settings)
        self.should_exit: bool = False

    def initialize_map(self) -> list[list[str]]:
        game_map: list[list[str]] = [[' ' for x in range(self.size[0])] for y in range(self.size[1])]

        game_map[0][0] = "┌"
        game_map[0][self.size[0] - 1] = "┐"
        game_map[self.size[1] - 1][0] = "└"
        game_map[self.size[1] - 1][self.size[0] - 1] = "┘"
        for x in range(1, self.size[0] - 1):
            game_map[0][x] = "─"
            game_map[self.size[1] - 1][x] = "─"

        for y in range(1, self.size[1] - 1):
            game_map[y][0] = "│"
            game_map[y][self.size[0] - 1] = "│"
        return game_map

    def draw(self) -> None:
        print('\033[H', end='')
        for line in self.map:
            print("".join(line))
        self.player.draw(self.map)
        self.apple.draw(self.map)

    def update(self) -> MenuType:
        self.draw()
        self.player.move()
        self.player.check_collision(self.size)
        self.apple.update(self.player)
        if not self.player.alive:
            print("Game Over")
        if self.should_exit:
            return MenuType.MAIN

    def handle_key(self, keyboardEvent: KeyboardEvent) -> None:
        if keyboardEvent.name == 'esc':
            self.should_exit = True
            return
        self.player.change_direction(keyboardEvent)