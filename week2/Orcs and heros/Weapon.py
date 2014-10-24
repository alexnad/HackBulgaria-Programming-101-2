import random


class Weapon:
    def __init__(self, w_type, damage, crit):
        self.w_type = w_type
        self.damage = damage
        self.crit = self.__set_crit(crit)

    def __set_crit(self, crit):
        if crit > 1 or crit < 0:
            raise ValueError
        return crit

    def critical_hit(self):
        return random.random() < self.crit
