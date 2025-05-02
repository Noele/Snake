import time

from keyboard import KeyboardEvent

from config.Colours import Colours
from config.Settings import Settings


class Player:
    def __init__(self, settings: Settings):
        self.head_colour = settings.snake_head_colour
        self.tail_colour = settings.snake_tail_colour

        self.position: tuple[int, int] = (5, 5)
        self.last_position: tuple[int, int] = (0, 0)

        self.tail_position: list[tuple[int, int]] = [(2, 5), (3, 5), (4, 5)]
        self.last_tail_position: list[tuple[int, int]] = []

        self.direction: tuple[int, int] = (1, 0)
        self.queued_direction: tuple[int, int] = (1, 0)
        self.direction_map:  dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
            'w': ((0, -1), (0, 1)),   # (new_direction, opposite_direction)
            's': ((0, 1), (0, -1)),
            'a': ((-1, 0), (1, 0)),
            'd': ((1, 0), (-1, 0))
        }

        self.speed: float = 0.25  # How much time in seconds, it takes for the player to move 1 space
        self.last_time_moved: float = 0

        self.alive = True

    def draw(self, map: list[list[str]]) -> None:
        map[self.last_position[1]][self.last_position[0]] = " "
        for segment in self.last_tail_position:
            map[segment[1]][segment[0]] = " "

        x, y = self.position
        map[y][x] = f"{self.head_colour}o{Colours.RESET}"
        for segment in self.tail_position:
            map[segment[1]][segment[0]] = f"{self.tail_colour}o{Colours.RESET}"

    def grow(self) -> None:
        self.tail_position.insert(0, (self.tail_position[0][0], self.tail_position[0][1]))

    def change_direction(self, keyboardEvent: KeyboardEvent) -> None:
        if keyboardEvent.name in self.direction_map:
            new_direction, opposite = self.direction_map[keyboardEvent.name]
            if self.direction != opposite:
                self.queued_direction = new_direction

    def move(self) -> None:
        if self.last_time_moved + self.speed < time.time() and self.alive:
            self.last_time_moved = time.time()

            self.direction = self.queued_direction

            self.last_position = self.position
            self.last_tail_position = self.tail_position.copy()

            self.position = tuple(a + b for a, b in zip(self.position, self.direction))

            for i in range(len(self.tail_position) - 1):
                self.tail_position[i] = self.tail_position[i + 1]
            self.tail_position[-1] = self.last_position

    def check_collision(self, map_size: tuple[int, int]) -> None:
        if self.position[0] <= 0 or self.position[0] >= map_size[0] - 1 or self.position[1] <= 0 or self.position[1] >= map_size[1] - 1:
            self.alive = False
        for segment in self.tail_position:
            if self.position == segment:
                self.alive = False
