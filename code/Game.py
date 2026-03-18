import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT, MENU
from code.GameOver import GameOver
from code.Menu import Menu
from code.Level import Level
from code.WinScreen import WinScreen


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # 🔥 garante controle de áudio
        self.window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == "GAME":

                current_level = 1

                while True:

                    level = Level(self.window, f"Level{current_level}")

                    result = level.run()

                    # 🔴 GAME OVER
                    if result == "gameover":
                        pygame.mixer.stop()
                        pygame.mixer.music.stop()
                        GameOver(self.window).run()
                        break

                    # 🟢 PASSOU DE FASE
                    current_level += 1

                    # 🏆 TERMINOU O JOGO (após level 3)
                    if current_level > 3:
                        pygame.mixer.stop()
                        pygame.mixer.music.stop()
                        WinScreen(self.window).run()
                        break