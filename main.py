from game.game import Game
from menu.menu import MenuType
from main_menu.main_menu import MainMenu
from menu.menu import Menu
import keyboard
import time

from config.settings import Settings
from settings_menus.astar_menu import AstarMenu
from settings_menus.difficulty_menu import DifficultyMenu
from settings_menus.mapsize_menu import MapsizeMenu
from settings_menus.settings_menu import SettingsMenu
from settings_menus.skins_menu import SkinsMenu


class Main:
    def __init__(self):
        self.settings: Settings = Settings()
        self.menus:  dict[MenuType, Menu] = {
            MenuType.MAIN: MainMenu,
            MenuType.GAME: Game,
            MenuType.SETTINGS: SettingsMenu,
            MenuType.DIFFICULTY: DifficultyMenu,
            MenuType.SKINS: SkinsMenu,
            MenuType.MAP: MapsizeMenu,
            MenuType.ASTAR: AstarMenu
        }
        self.FRAME_TIME: float = 1 / self.settings.fps
        self.previous_time: float = time.time()

        self.current_menu: Menu = MainMenu(self.settings)
        keyboard.on_press(self.current_menu.handle_key)
        self.running = True

    def run(self) -> None:
        print("\033[?25l", end="")  # Hide the cursor
        while self.running:
            self.current_menu.update()
            current_time: float = time.time()
            delta_time: float = current_time - self.previous_time

            if delta_time >= self.FRAME_TIME:
                menu: MenuType = self.current_menu.update()
                if menu == MenuType.EXIT:
                    self.running = False
                elif menu in self.menus:
                    self.current_menu = self.menus.get(menu)(self.settings)
                    keyboard.on_press(self.current_menu.handle_key)
                self.previous_time = current_time
        print("\033[?25h", end="")  # Show the cursor


if __name__ == "__main__":
    main = Main()
    main.run()
