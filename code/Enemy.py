from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, speed: int):  # 3 parâmetros + self
        super().__init__(name, position)
        self.speed = speed

    def move(self):
        self.rect.centerx -= self.speed
