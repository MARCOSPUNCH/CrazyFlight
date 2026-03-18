import pygame

from code.Const import C_RED


class WinScreen:
    def __init__(self, screen):
        self.screen = screen

        # fundo
        self.background = pygame.image.load('./asset/YouWon0.png').convert()

        # imagem transparente
        self.foreground = pygame.image.load('./asset/YouWon.png').convert_alpha()

        # escala
        self.background = pygame.transform.scale(self.background, (576, 324))
        self.foreground = pygame.transform.scale(self.foreground, (576, 324))
        self.font = pygame.font.Font('./asset/DeathStar.otf', 60)
        self.text = self.font.render("Congratulations", True, (C_RED))

        # som (SEM os.path, direto)
        self.sound = pygame.mixer.Sound('./asset/YouWon.wav')

    def run(self):
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        # 🔥 garante que o som toca
        pygame.mixer.stop()
        self.sound.play()

        running = True
        while running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # 🔥 ordem correta
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.foreground, (0, 0))
            text_rect = self.text.get_rect(center=(288, 50))
            self.screen.blit(self.text, text_rect)

            pygame.display.update()

            # 4 segundos
            if current_time - start_time > 4000:
                running = False

            clock.tick(60)
