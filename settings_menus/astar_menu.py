from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class AstarMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.options: list[bool] = [True, False]

    def draw(self) -> None:
        print('\033[H', end='')
        print(f"""
┌────────────────────┐
│        Astar       │
│    {self.selected_colour if self.selected_option == 0 else ""}  Activate  {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 1 else ""} Deactivate {self.reset_colour}    │
└────────────────────┘
        """
              )

    def update(self) -> MenuType:
        self.draw()
        if self.enter_selection:
            self.settings.use_astar = self.options[self.selected_option]
            return MenuType.SETTINGS
        if self.exit_menu:
            return MenuType.SETTINGS