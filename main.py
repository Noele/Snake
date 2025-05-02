from game.Game import Game
from menu.Menu import MenuType
from main_menu.MainMenu import MainMenu
from menu.Menu import Menu
import keyboard
import time

from config.Settings import Settings


class Main:
    def __init__(self):
        self.settings = Settings()

        self.FRAME_TIME: float = 1 / self.settings.fps
        self.previous_time: float = time.time()

        self.current_menu: Menu = MainMenu(self.settings)
        keyboard.on_press(self.current_menu.handle_key)
        self.running = True

    def run(self) -> None:
        while self.running:
            self.current_menu.update()
            current_time: float = time.time()
            delta_time: float = current_time - self.previous_time

            if delta_time >= self.FRAME_TIME:
                menu: MenuType = self.current_menu.update()
                match menu:
                    case MenuType.MAIN:
                        self.current_menu = MainMenu(self.settings)
                        keyboard.on_press(self.current_menu.handle_key)
                    case MenuType.GAME:
                        self.current_menu = Game(self.settings)
                        keyboard.on_press(self.current_menu.handle_key)
                    case MenuType.EXIT:
                        self.running = False

                self.previous_time = current_time


if __name__ == "__main__":
    main = Main()
    main.run()
