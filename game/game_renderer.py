from game.Model.apple import Apple
from game.Model.player import Player


class GameRenderer:
    HORIZONTAL_BORDER: str = "─"
    VERTICAL_BORDER: str = "│"
    TOP_LEFT_CORNER: str = "┌"
    TOP_RIGHT_CORNER: str = "┐"
    BOTTOM_LEFT_CORNER: str = "└"
    BOTTOM_RIGHT_CORNER: str = "┘"

    def __init__(self, size: tuple[int, int], player: Player, apple: Apple):
        self.size: tuple[int, int] = size
        self.map: list[list[str]] = self._initialize_map()

        self.player: Player = player
        self.apple: Apple = apple

    def _initialize_map(self) -> list[list[str]]:
        game_map: list[list[str]] = [[' ' for x in range(self.size[0])] for y in range(self.size[1])]

        game_map[0][0] = self.TOP_LEFT_CORNER
        game_map[0][self.size[0] - 1] = self.TOP_RIGHT_CORNER
        game_map[self.size[1] - 1][0] = self.BOTTOM_LEFT_CORNER
        game_map[self.size[1] - 1][self.size[0] - 1] = self.BOTTOM_RIGHT_CORNER
        for x in range(1, self.size[0] - 1):
            game_map[0][x] = self.HORIZONTAL_BORDER
            game_map[self.size[1] - 1][x] = self.HORIZONTAL_BORDER

        for y in range(1, self.size[1] - 1):
            game_map[y][0] = self.VERTICAL_BORDER
            game_map[y][self.size[0] - 1] = self.VERTICAL_BORDER
        return game_map

    def draw(self, astar_path: list[list[int, int]] = None) -> None:
        print('\033[H', end='')
        if astar_path:
            for x, y in astar_path:
                self.map[y][x] = '*'

        self.player.draw(self.map)
        self.apple.draw(self.map)

        for index, line in enumerate(self.map):
            if index == 0 or index == self.size[0] - 1:
                print(self.HORIZONTAL_BORDER.join(line))
            else:
                print(" ".join(line))

        if astar_path:
            for x, y in astar_path:
                if self.map[y][x] == '*':
                    self.map[y][x] = ' '
