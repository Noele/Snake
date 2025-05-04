from config.colours import Colours


class Settings:
    def __init__(self):
        self.snake_head_colour: str = Colours.RED
        self.snake_tail_colour: str = Colours.GREEN
        self.apple_colour: str = Colours.RED
        self.game_size: tuple[int, int] = (30, 30)
        self.fps: int = 20
        self.player_speed: float = 0.125
        self.use_astar: bool = False
