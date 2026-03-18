import pygame


class GameOver:
    def __init__(self, screen):
        self.screen = screen

        # FUNDO
        self.background0 = pygame.image.load('./asset/GameOver0.png').convert()
        self.background0 = pygame.transform.scale(self.background0, (576, 324))

        # IMAGEM POR CIMA
        self.background = pygame.image.load('./asset/GameOver.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (576, 324))

        # TEXTO
        self.font = pygame.font.Font('./asset/DeathStar.otf', 60)
        self.text = self.font.render("TRY AGAIN", True, (255, 0, 0))

        # SOM
        self.sound = pygame.mixer.Sound('./asset/GameOver.ogg')

    def run(self):
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        pygame.mixer.stop()
        self.sound.play()

        running = True
        while running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # desenha
            self.screen.blit(self.background0, (0, 0))
            self.screen.blit(self.background, (0, 0))

            text_rect = self.text.get_rect(center=(288, 50))
            self.screen.blit(self.text, text_rect)

            pygame.display.flip()

            # 🔥 ESSENCIAL (voltar pro menu)
            if current_time - start_time > 4000:
                running = False

            clock.tick(60)