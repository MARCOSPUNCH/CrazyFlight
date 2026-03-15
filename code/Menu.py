import pygame.image
from pygame import Surface
from pygame.font import Font

from code.Const import C_GREEN, C_RED, MENU, C_YELLOW, C_DARK_BLUE, SCR_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        pass

    def run(self, menu_index=0):

        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(self.surf, self.rect)

            self.menu_text(100, "Crazy", C_GREEN, (SCR_WIDTH / 2, 70))
            self.menu_text(100, "Flight", C_GREEN, (SCR_WIDTH / 2, 160))

            for i in range(len(MENU)):

                if i == menu_index:
                    self.menu_text(30, MENU[i], C_DARK_BLUE, (SCR_WIDTH / 2, 210 + 30 * i))
                else:
                    self.menu_text(30, MENU[i], C_RED, (SCR_WIDTH / 2, 210 + 30 * i))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.mixer_music.stop()
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        menu_index = (menu_index + 1) % len(MENU)

                    if event.key == pygame.K_UP:
                        menu_index = (menu_index - 1) % len(MENU)

                    if event.key == pygame.K_RETURN:

                        if menu_index == 0:  # START GAME
                            pygame.mixer_music.stop()
                            return "GAME"

                        if menu_index == 1:  # EXIT
                            pygame.mixer_music.stop()
                            pygame.quit()
                            quit()

            pygame.display.flip()

    def menu_text(self, tex_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("asset/DeathStar.otf", tex_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
