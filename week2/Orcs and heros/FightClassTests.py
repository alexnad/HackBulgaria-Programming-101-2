import unittest
from OrcClass import Orc
from HeroClass import Hero
from Weapon import Weapon
from Fight import Fight


class TestFightClass(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Arthas', 3500, 'Lich King')
        self.orc = Orc('Garrosh', 3500, 1.2)
        self.frostmourne = Weapon('Sword', 250, 0.8)
        self.gorehowl = Weapon('Axe', 350, 0.2)
        self.hero.equip_weapon(self.frostmourne)
        self.orc.equip_weapon(self.gorehowl)

        self.fight = Fight(self.hero, self.orc)

    def test_initialing(self):
        self.assertIsInstance(self.fight.hero, Hero)
        self.assertIsInstance(self.fight.orc, Orc)

    def test_who_is_first(self):
        first = []
        for i in range(10):
            self.fight = Fight(self.hero, self.orc)
            first.append(self.fight.first)

        flag = [False, False]
        for i in first:
            if isinstance(i, Hero):
                flag[0] = True
            elif isinstance(i, Orc):
                flag[1] = True

        self.assertEqual(flag, [True, True])

    def test_simulate_fight_Hero_Wins(self):
        self.orc = Orc('Gul Dan', 500, 1)
        self.fight = Fight(self.hero, self.orc)
        self.assertEqual(self.fight.simulate_fight(), 'hero wins')

    def test_simulate_fight_Orc_Wins(self):
        self.hero = Hero('Tirion', 500, 'The AshBringer')
        self.fight = Fight(self.hero, self.orc)
        self.assertEqual(self.fight.simulate_fight(), 'orc wins')

    def test_simulate_first_wins(self):
        self.hero = Hero('Tirion', 1000, 'The AshBringer')
        self.orc = Orc('Gul Dan', 1000, 1)
        weapon = Weapon('Sword', 200, 0)
        self.hero.equip_weapon(weapon)
        self.orc.equip_weapon(weapon)
        self.fight = Fight(self.hero, self.orc)
        if isinstance(self.fight.first, Hero):
            winer = 'hero wins'
        else:
            winer = 'orc wins'
        self.assertEqual(self.fight.simulate_fight(), winer)

if __name__ == "__main__":
    unittest.main()
