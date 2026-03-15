import random
import sys
import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

        # Criar background e player
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))

        # Controle de spawn
        self.spawn_time = 0
        self.spawn_delay = 2000  # tempo em ms entre inimigos
        self.BUFFER = 50  # espaço para remover inimigos fora da tela

    def run(self):
        # Tocar música
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()

            # Spawn de inimigos
            if current_time - self.spawn_time > self.spawn_delay:
                enemy_types = [
                    'BalloonEnemy',
                    'BirdEnemy1', 'BirdEnemy2', 'BirdEnemy3', 'BirdEnemy4',
                    'PlaneEnemy1', 'PlaneEnemy2', 'PlaneEnemy3', 'PlaneEnemy4',
                    'PlaneEnemy5', 'PlaneEnemy6', 'PlaneEnemy7', 'PlaneEnemy8',
                    'UfoEnemy'
                ]

                enemy_name = random.choice(enemy_types)
                enemy_y = random.randint(0, SCR_HEIGHT - 50)
                enemy = EntityFactory.get_entity(enemy_name, (SCR_WIDTH, enemy_y))
                if enemy:
                    self.entity_list.append(enemy)
                self.spawn_time = current_time

            # Atualizar e desenhar entidades
            for ent in self.entity_list[:]:  # percorre uma cópia da lista
                # Movimentar inimigos (exceto Player)
                if not isinstance(ent, Player):
                    ent.move()
                    self.window.blit(ent.surf, ent.rect)

                    # Remover inimigos que saíram da tela
                    if isinstance(ent, Enemy) and ent.rect.right < -self.BUFFER:
                        self.entity_list.remove(ent)

            # Desenhar player por cima
            player = next((e for e in self.entity_list if isinstance(e, Player)), None)
            if player:
                player.move()
                self.window.blit(player.surf, player.rect)

            # Eventos do pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
