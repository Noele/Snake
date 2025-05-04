from config.colours import Colours
from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class SkinsMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.options: list[tuple[Colours, Colours]] = [(Colours.BLACK, Colours.BRIGHT_BLACK), (Colours.GREEN, Colours.YELLOW),
                        (Colours.CYAN, Colours.BRIGHT_MAGENTA), (Colours.YELLOW, Colours.RED),
                        (Colours.GREEN, Colours.RED)]

    def draw(self) -> None:
        print('\033[H', end='')
        print(f"""
┌────────────────────┐
│        Skins       │
│    {self.selected_colour if self.selected_option == 0 else ""}   Stealth  {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 1 else ""}    Camo    {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 2 else ""}  Bubblegum {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 3 else ""}   Sunset   {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 4 else ""}   Default  {self.reset_colour}    │
└────────────────────┘
        """
              )

    def update(self) -> MenuType:
        self.draw()
        if self.enter_selection:
            self.settings.snake_tail_colour = self.options[self.selected_option][0]
            self.settings.snake_head_colour = self.options[self.selected_option][1]
            return MenuType.SETTINGS
        if self.exit_menu:
            return MenuType.SETTINGS

