from menu.menu import MenuType
from menu.menu import Menu
from config.settings import Settings


class DifficultyMenu(Menu):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.options: list[float] = [0.25, 0.125, 0.050] # Easy, Medium, Hard | Numbers effect player speed

    def draw(self) -> None:
        print('\033[H', end='')
        print(f"""
┌────────────────────┐
│     Difficulty     │
│    {self.selected_colour if self.selected_option == 0 else ""}    Easy    {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 1 else ""}   Normal   {self.reset_colour}    │
│    {self.selected_colour if self.selected_option == 2 else ""}    Hard    {self.reset_colour}    │
└────────────────────┘
        """
              )

    def update(self) -> MenuType:
        self.draw()
        if self.enter_selection:
            self.settings.player_speed = self.options[self.selected_option]
            return MenuType.SETTINGS
        if self.exit_menu:
            return MenuType.SETTINGS

