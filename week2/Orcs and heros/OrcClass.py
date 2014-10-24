from Entity import Entity
import random


class Orc(Entity):
    def __init__(self, name, health, barserk):
        super().__init__(name, health)
        self.barserk = self.__set_up_barserk(barserk)
        self.barserk_mode_on = False
        self.barserk_attacks = 0

    def __set_up_barserk(self, barserk):
        if barserk < 1:
            return 1
        elif barserk > 2:
            return 2
        else:
            return barserk

    def attack(self):
        if self.weapon:
            turn_on_barserk = self.barserk > 1+random.random()
            if turn_on_barserk and self.barserk_attacks == 0:
                    self.barserk_attacks = 2

            if self.weapon.critical_hit():
                if self.barserk_attacks > 0:
                    self.barserk_attacks -= 1
                    return self.weapon.damage * 3
            if self.barserk_attacks > 0:
                self.barserk_attacks -= 1
                return self.weapon.damage * 1.5

            return self.weapon.damage

        return 0
