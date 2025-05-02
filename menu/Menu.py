import os

from keyboard import KeyboardEvent
from config.Settings import Settings
from menu.MenuType import MenuType


class Menu:
    def __init__(self, settings: Settings):
        self.settings = settings
        os.system('cls' if os.name == 'nt' else 'clear')

    def update(self) -> MenuType:
        raise NotImplementedError("Update() not implemented")

    def handle_key(self,  keyboardEvent: KeyboardEvent) -> None:
        raise NotImplementedError("handle_key() not implemented")