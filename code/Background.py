from code.Const import SCR_WIDTH, SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position : tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = SCR_WIDTH
