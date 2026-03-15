
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU
from code.Menu import Menu
from code.Level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == "GAME":
                level = Level(self.window, "Level1")
                level.run()