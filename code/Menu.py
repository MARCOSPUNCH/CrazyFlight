import sys

import pygame.image
from pygame import Surface
from pygame.font import Font

from code.Const import C_GREEN, C_RED, MENU, C_YELLOW, C_DARK_BLUE, SCR_WIDTH, ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, menu_index=0):

        # 🔊 música do menu
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)

        while True:

            # desenha fundo
            self.window.blit(self.surf, self.rect)

            # títulos
            self.menu_text(100, "Crazy", C_GREEN, (SCR_WIDTH / 2, 70))
            self.menu_text(100, "Flight", C_GREEN, (SCR_WIDTH / 2, 160))

            # opções do menu
            for i in range(len(MENU)):
                color = C_DARK_BLUE if i == menu_index else C_RED
                self.menu_text(30, MENU[i], color, (SCR_WIDTH / 2, 210 + 30 * i))

            # 🔥 instruções do jogo no canto inferior esquerdo
            instr_font = pygame.font.Font('./asset/DeathStar.otf', 12)
            instructions = [
                "UP = move up",
                "DOWN = move down",
                "LEFT = move left",
                "RIGHT = move right",
                "SPACE + RIGHT = turbo"
            ]

            for i, line in enumerate(instructions):
                instr_text = instr_font.render(line, True, ORANGE)
                self.window.blit(instr_text, (10, 220 + i * 18))  # 18 px de espaçamento entre linhas

            # eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_index = (menu_index + 1) % len(MENU)
                    if event.key == pygame.K_UP:
                        menu_index = (menu_index - 1) % len(MENU)
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        if menu_index == 0:  # START GAME
                            return "GAME"
                        if menu_index == 1:  # EXIT
                            pygame.quit()
                            sys.exit()

            # atualiza tela
            pygame.display.flip()

    def menu_text(self, tex_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("asset/DeathStar.otf", tex_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
