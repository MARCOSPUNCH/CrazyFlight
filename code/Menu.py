import pygame.image
from pygame import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, C_GREEN, C_RED, MENU


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

        pass

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "Crazy", (C_GREEN), ((WIN_WIDTH / 2), 70))
            self.menu_text(100, "Flight", (C_GREEN), ((WIN_WIDTH / 2), 160))

            for i in range(len(MENU)):
                self.menu_text(30, MENU[i], C_RED, ((WIN_WIDTH / 2), 210 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, tex_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("asset/DeathStar.otf", tex_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
