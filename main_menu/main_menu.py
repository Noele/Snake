from keyboard import KeyboardEvent

from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class MainMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.enter_game = False
        self.exit = False
        self.enter_settings = False

    def draw(self) -> None:
        print('\033[H', end='')
        print(
"""
┌────────────────────────────┐
│          Main menu         │
│   Press Enter to start.    │
│  Press S to open settings. │
│   Press ESC to exit.       │
└────────────────────────────┘
""")

    def update(self) -> MenuType:
        self.draw()
        if self.enter_game:
            return MenuType.GAME
        if self.exit:
            return MenuType.EXIT
        if self.enter_settings:
            return MenuType.SETTINGS

    def handle_key(self, keyboardEvent: KeyboardEvent) -> None:
        if keyboardEvent.name == 'enter':
            self.enter_game = True
        if keyboardEvent.name == 'esc':
            self.exit = True
        if keyboardEvent.name == 's':
            self.enter_settings = True

