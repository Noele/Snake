from keyboard import KeyboardEvent

from menu.Menu import MenuType
from menu.Menu import Menu
from config.Settings import Settings


class MainMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.enter_game = False
        self.exit = False

    def draw(self) -> None:
        print('\033[H', end='')
        print(
"""
┌────────────────────────────┐
│          Main menu         │
│   Press Enter to start.    │
└────────────────────────────┘
""")

    def update(self) -> MenuType:
        self.draw()
        if self.enter_game:
            return MenuType.GAME
        if self.exit:
            return MenuType.EXIT

    def handle_key(self, keyboardEvent: KeyboardEvent) -> None:
        if keyboardEvent.name == 'enter':
            self.enter_game = True
        if keyboardEvent.name == 'esc':
            self.exit = True

