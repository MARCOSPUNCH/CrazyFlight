from code.Entity import Entity


class Obstacle:
    def __init__(self, entity_list: list[Entity]):
        self.entity_list = entity_list
        