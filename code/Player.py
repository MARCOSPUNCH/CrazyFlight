import pygame

from code.Entity import Entity
from code.Const import PLAYER_SPEED, PLAYER_BOOST, SCR_WIDTH, SCR_HEIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = PLAYER_SPEED
        self.boost = PLAYER_BOOST

    def move(self):
        keys = pygame.key.get_pressed()

        # velocidade padrão
        speed = self.speed

        # turbo
        if keys[pygame.K_SPACE]:
            speed = self.boost

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += speed

        # limites da tela
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCR_WIDTH:
            self.rect.right = SCR_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > SCR_HEIGHT:
            self.rect.bottom = SCR_HEIGHT
