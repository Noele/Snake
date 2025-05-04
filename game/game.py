from keyboard import KeyboardEvent

from Pathfinding.astar import astar
from game.Model.apple import Apple
from game.Model.player import Player
from game.game_renderer import GameRenderer
from menu.menu import MenuType

from menu.menu import Menu

from config.settings import Settings


class Game(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.size: tuple[int, int] = self.settings.game_size
        self.player: Player = Player(self.settings)
        self.apple: Apple = Apple(self.settings, self.player)
        self.should_exit: bool = False
        self.renderer: GameRenderer = GameRenderer(self.size, self.player, self.apple)

    def update(self) -> MenuType:
        if self.settings.use_astar:
            astar_path = self.generate_astar_path()
            self.renderer.draw(astar_path)
            next_step = self.get_next_step(astar_path)
        else:
            next_step = None
            self.renderer.draw(None)

        self.player.move(next_step)
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

    def get_next_step(self, path) -> tuple[int, int] | None:
        if path == [] or path is None:
            next_step = None
        else:
            next_step = (path[0][0], path[0][1])
        return next_step

    def generate_astar_path(self) -> list[list[int, int]]:
        astarmap = []
        for yindex, y in enumerate(self.renderer.map):
            row = []
            for xindex, x in enumerate(y):
                if (xindex, yindex) in self.player.tail_position:
                    row.append(1)
                elif (xindex, yindex) == self.player.position:
                    row.append(3)
                elif (xindex, yindex) == self.apple.position:
                    row.append(4)
                elif x != " ":
                    row.append(1)
                else:
                    row.append(0)

            astarmap.append(row)
        return astar(astarmap)
