import os
import random
import sys
import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT
from code.Const import LEVEL_DURATION, LEVEL_SPAWN_DELAY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:

    def __init__(self, window, name):

        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

        # Criar background
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        # Criar player
        self.entity_list.append(EntityFactory.get_entity('Player'))

        # Controle spawn
        self.spawn_time = 0
        self.spawn_delay = LEVEL_SPAWN_DELAY.get(self.name, 2000)

        # buffer para remover inimigos fora da tela
        self.BUFFER = 50

        # tempo do level
        self.level_start_time = pygame.time.get_ticks()
        self.level_duration = LEVEL_DURATION

    def run(self):

        music_path_mp3 = f'./asset/{self.name}.mp3'
        music_path_wav = f'./asset/{self.name}.wav'

        if os.path.exists(music_path_mp3):
            pygame.mixer.music.load(music_path_mp3)

        elif os.path.exists(music_path_wav):
            pygame.mixer.music.load(music_path_wav)

        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            current_time = pygame.time.get_ticks()

            # fim do level
            if current_time - self.level_start_time > self.level_duration:
                pygame.mixer.stop()  # 🔥 ADICIONA ISSO
                pygame.mixer.music.stop()  # (pode manter)
                return "next"

            # spawn inimigos
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

            # atualizar entidades
            for ent in self.entity_list[:]:

                if not isinstance(ent, Player):

                    ent.move()

                    self.window.blit(ent.surf, ent.rect)

                    if isinstance(ent, Enemy) and ent.rect.right < -self.BUFFER:
                        self.entity_list.remove(ent)

            # desenhar player
            player = next((e for e in self.entity_list if isinstance(e, Player)), None)

            if player:
                player.move()
                self.window.blit(player.surf, player.rect)
                # colisão
                for ent in self.entity_list:
                    if isinstance(ent, Enemy):
                        if player.rect.colliderect(ent.rect):
                            pygame.mixer.stop()  # 🔥 ADICIONA ISSO
                            pygame.mixer.music.stop()
                            return "gameover"

            # eventos pygame
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
