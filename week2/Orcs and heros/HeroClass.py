from Entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def know_as(self):
        return '{0} the {1}'.format(self.name, self. nickname)
