import unittest
from HeroClass import Hero


class HeroClassTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Lord', 1000, 'GayLord')

    def test_hero_atributes(self):
        self.assertEqual(self.hero.name, 'Lord')
        self.assertEqual(self.hero.health, 1000)
        self.assertEqual(self.hero.nickname, 'GayLord')

    def test_know_as(self):
        self.assertEqual(self.hero.know_as(), "Lord the GayLord")


if __name__ == "__main__":
    unittest.main()
