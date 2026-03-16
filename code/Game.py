import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT, MENU
from code.Menu import Menu
from code.Level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == "GAME":

                current_level = 1

                while True:

                    level = Level(self.window, f"Level{current_level}")

                    level.run()

                    current_level += 1