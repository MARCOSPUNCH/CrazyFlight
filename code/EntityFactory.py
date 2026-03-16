import pygame
from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
from code.Const import SCR_WIDTH, SCR_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        # -------------------------
        # Background
        if entity_name in ['Level1Bg', 'Level2Bg', 'Level3Bg']:

            list_bg = []

            for i in range(4):
                list_bg.append(Background(f'{entity_name}{i}', (0, 0)))
                list_bg.append(Background(f'{entity_name}{i}', (SCR_WIDTH, 0)))

            return list_bg

        # -------------------------
        # Player
        # -------------------------
        if entity_name == 'Player':
            return Player('Player', (50, SCR_HEIGHT // 2))

        # -------------------------
        # Inimigos
        # -------------------------
        normal_enemies = [
            'BalloonEnemy',
            'BirdEnemy1', 'BirdEnemy2', 'BirdEnemy3', 'BirdEnemy4',
            'PlaneEnemy1', 'PlaneEnemy2', 'PlaneEnemy3', 'PlaneEnemy4',
            'PlaneEnemy5', 'PlaneEnemy6', 'PlaneEnemy7', 'PlaneEnemy8',
            'UfoEnemy'
        ]

        if entity_name in normal_enemies:
            # Velocidade padrão por tipo
            if entity_name == 'BalloonEnemy':
                enemy_speed = 1
            elif 'Bird' in entity_name:
                enemy_speed = 3
            elif 'Plane' in entity_name:
                enemy_speed = 4
            elif 'Ufo' in entity_name:
                enemy_speed = 5
            else:
                enemy_speed = 2  # fallback

            # Passa a velocidade como positional, evitando keyword error
            return Enemy(entity_name, position, enemy_speed)

        # Se não for reconhecido, retorna None
        return None
