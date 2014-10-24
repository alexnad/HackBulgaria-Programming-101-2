from OrcClass import Orc
from Weapon import Weapon
import unittest


class OrcTests(unittest.TestCase):
    def setUp(self):
        self.orc = Orc('Gul Dan', 2000, 1.7)

    def test_initialisation(self):
        self.assertEqual(self.orc.barserk, 1.7)
        self.assertEqual(self.orc.name, 'Gul Dan')
        self.assertEqual(self.orc.max_health, 2000)
        self.orc = Orc('Gul Dan', 2000, 2.5)
        self.assertEqual(self.orc.barserk, 2)
        self.orc = Orc('Gul Dan', 2000, 0.5)
        self.assertEqual(self.orc.barserk, 1)

    def test_orc_attack(self):
        self.orc = Orc('Gul Dan', 2000, 1)
        self.assertEqual(self.orc.attack(), 0)

        sword = Weapon('Sword', 100, 0)
        self.orc.equip_weapon(sword)
        self.assertEqual(self.orc.attack(), 100)

        self.orc = Orc('Gul Dan', 2000, 2)
        self.orc.equip_weapon(sword)
        self.assertEqual(self.orc.attack(), 150)

        sword = Weapon('Sword', 100, 1)
        self.orc.equip_weapon(sword)
        self.assertEqual(self.orc.attack(), 300)


if __name__ == "__main__":
    unittest.main()
