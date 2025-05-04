from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class MapsizeMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.options: list[tuple[int, int]] = [(15, 15), (30, 30), (60, 60)]

    def draw(self) -> None:
        print('\033[H', end='')
        print(f"""
┌────────────────────┐
│      Map Size      │
│    {self.selected_colour if self.selected_option == 0 else ""}    Small   {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 1 else ""}   Medium   {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 2 else ""}    Large   {self.reset_colour}    │
└────────────────────┘
        """
              )

    def update(self) -> MenuType:
        self.draw()
        if self.enter_selection:
            self.settings.game_size = self.options[self.selected_option]
            return MenuType.SETTINGS
        if self.exit_menu:
            return MenuType.SETTINGS