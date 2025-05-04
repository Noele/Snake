from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class SettingsMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.options: list[MenuType] = [MenuType.DIFFICULTY, MenuType.SKINS, MenuType.MAP, MenuType.ASTAR]

    def draw(self) -> None:
        print('\033[H', end='')
        print(f"""
┌────────────────────┐
│      Settings      │
│    {self.selected_colour if self.selected_option == 0 else ""} Difficulty {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 1 else ""}   Skins    {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 2 else ""}  Map Size  {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 3 else ""}     A*     {self.reset_colour}    │
└────────────────────┘
        """
              )

    def update(self) -> MenuType:
        self.draw()
        if self.enter_selection:
            return self.options[self.selected_option]
        if self.exit_menu:
            return MenuType.MAIN
