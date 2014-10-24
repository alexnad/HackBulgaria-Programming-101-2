import unittest
from Entity import Entity
from Weapon import Weapon


class TestEntityClass(unittest.TestCase):
    def setUp(self):
        self.entity = Entity('Baba', 100)

    def test_initialisation_atributes(self):
        self.assertEqual(self.entity.name, 'Baba')
        self.assertEqual(self.entity.health, 100)

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())
        self.entity = Entity('Baba', 0)
        self.assertFalse(self.entity.is_alive())

    def test_take_damage(self):
        self.assertTrue(self.entity.take_damage(50))
        self.assertEqual(self.entity.get_health(), 50)

        self.assertTrue(self.entity.take_damage(51))
        self.assertEqual(self.entity.get_health(), 0)
        self.assertFalse(self.entity.take_damage(10))

    def test_take_healing(self):
        self.assertTrue(self.entity.take_healing(100))
        self.assertEqual(self.entity.get_health(), 100)
        self.entity.take_damage(50)
        self.assertTrue(self.entity.take_healing(40))
        self.assertEqual(self.entity.get_health(), 90)

        self.entity = Entity('Baba', 0)
        self.assertFalse(self.entity.take_healing(100))

    def test_has_weapon(self):
        self.assertFalse(self.entity.has_weapon())

    def test_equip_weapon(self):
        sword = Weapon('Sword', 100, 0.4)
        sword2 = Weapon('Sword', 100, 0.4)
        self.entity.equip_weapon(sword)
        self.assertTrue(self.entity.has_weapon())
        self.assertEqual(self.entity.weapon, sword)
        self.entity.equip_weapon(sword2)
        self.assertNotEqual(self.entity.weapon, sword)

    def test_attack(self):
        self.assertEqual(self.entity.attack(), 0)
        sword = Weapon('Sword', 100, 0)
        self.entity.equip_weapon(sword)
        self.assertEqual(self.entity.attack(), 100)

        sword = Weapon('Sword', 100, 1)
        self.entity.equip_weapon(sword)
        self.assertEqual(self.entity.attack(), 200)


if __name__ == "__main__":
    unittest.main()
