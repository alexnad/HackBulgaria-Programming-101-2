import unittest
from Weapon import Weapon


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon('Sword', 150, 0.5)

    def test_initialisation(self):
        self.assertEqual(self.weapon.w_type, 'Sword')
        self.assertEqual(self.weapon.damage, 150)
        self.assertEqual(self.weapon.crit, 0.5)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.weapon = Weapon('Sword', 150, 2.5)

    def test_critical_hit(self):
        crit_hits = []
        for i in range(20):
            crit_hits.append(self.weapon.critical_hit())

        flag = [False, False]
        for i in crit_hits:
            if i:
                flag[0] = True
            if not i:
                flag[1] = True

        self.assertEqual(flag, [True, True])


if __name__ == "__main__":
    unittest.main()
