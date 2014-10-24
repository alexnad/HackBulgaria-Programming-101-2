from OrcClass import Orc
from HeroClass import Hero
from random import randint


class Fight:
    def __init__(self, oponent1, oponent2):
        self.hero = self.__get_hero(oponent1, oponent2)
        self.orc = self.__get_orc(oponent1, oponent2)
        self.first = self.assign_first()

    def __get_hero(self, oponent1, oponent2):
        if isinstance(oponent1, Hero):
            return oponent1
        return oponent2

    def __get_orc(self, oponent1, oponent2):
        if isinstance(oponent1, Orc):
            return oponent1
        return oponent2

    def assign_first(self):
        if randint(1, 100) > 50:
            return self.hero
        else:
            return self.orc

    def simulate_fight(self):
        while self.hero.is_alive() and self.orc.is_alive():
            if self.first == self.hero:
                self.orc.take_damage(self.hero.attack())
                self.first = self.orc
            else:
                self.hero.take_damage(self.orc.attack())
                self.first = self.hero
            print('{0} hp: {1} \n{2} hp: {3}'.format(self.hero.know_as(), self.hero.get_health(), self.orc.name, self.orc.get_health()))

        if self.hero.is_alive():
            return 'hero wins'

        else:
            return 'orc wins'
