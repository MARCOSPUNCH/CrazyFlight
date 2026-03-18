

# C
C_GREEN = (0 ,255, 0)
C_RED = (255, 0, 0)
C_YELLOW = (255, 255, 0)
C_DARK_BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)


# -----------------------------
# TELA
# -----------------------------
SCR_WIDTH = 576
SCR_HEIGHT = 324


# -----------------------------
# PLAYER
# -----------------------------
PLAYER_SPEED = 4
PLAYER_BOOST = 16


# -----------------------------
# MENU
# -----------------------------
MENU = [
    'START GAME',
    'EXIT',
]


# -----------------------------
# BACKGROUND PARALLAX
# -----------------------------
SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 4,
    'Level1Bg3': 6,

    # LEVEL 2
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 4,
    'Level2Bg3': 6,

    # LEVEL 3
    'Level3Bg0': 0,
    'Level3Bg1': 2,
    'Level3Bg2': 4,
    'Level3Bg3': 6,

}


# -----------------------------
# VELOCIDADE DOS INIMIGOS
# -----------------------------
ENEMY_SPEED = {
    'BalloonEnemy': 1,
    'BirdEnemy1': 3,
    'BirdEnemy2': 3,
    'BirdEnemy3': 3,
    'BirdEnemy4': 3,
    'DragonEnemy': 4,
    'PlaneEnemy1': 5,
    'PlaneEnemy2': 5,
    'PlaneEnemy3': 5,
    'PlaneEnemy4': 5,
    'PlaneEnemy5': 5,
    'PlaneEnemy6': 5,
    'PlaneEnemy7': 5,
    'PlaneEnemy8': 5,
    'UfoEnemy': 4
}


# -----------------------------
# SISTEMA DE LEVEL
# -----------------------------

# duração do level (20s)
LEVEL_DURATION = 20000


# tempo de spawn por level
LEVEL_SPAWN_DELAY = {
    "Level1": 2000,
    "Level2": 1500,
    "Level3": 1000
}