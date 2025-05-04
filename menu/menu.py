import os

from keyboard import KeyboardEvent
from config.settings import Settings
from menu.menu_type import MenuType


class Menu:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.exit_menu: bool = False
        self.enter_selection: bool = False
        self.selected_colour: str = "\033[42m"
        self.reset_colour: str = "\033[0m"
        self.selected_option = 0
        self.enter_selection: bool = False
        self.options = None
        os.system('cls' if os.name == 'nt' else 'clear')

    def update(self) -> MenuType:
        raise NotImplementedError("Update() not implemented")

    def handle_key(self, keyboardEvent: KeyboardEvent) -> None:
        if keyboardEvent.name == 's':
            self.selected_option += 1
        if keyboardEvent.name == 'w':
            self.selected_option -= 1
        if self.selected_option > len(self.options) -1:
            self.selected_option = len(self.options) -1
        if self.selected_option < 0:
            self.selected_option = 0
        if keyboardEvent.name == 'enter':
            self.enter_selection = True
        if keyboardEvent.name == 'esc':
            self.exit_menu = True