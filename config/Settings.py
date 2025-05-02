from config.Colours import Colours


class Settings:
    def __init__(self):
        self.snake_head_colour: str = Colours.RED
        self.snake_tail_colour: str = Colours.GREEN
        self.apple_colour: str = Colours.RED
        self.game_size: tuple[int, int] = (30, 10)
        self.fps: int = 20