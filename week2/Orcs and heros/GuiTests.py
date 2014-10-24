import unittest
from GUI import Player, Game
from HeroClass import Hero
from OrcClass import Orc


class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Baba', 2000, 'Yaga')
        self.player = Player('player_1', self.hero)

    def test_initialisation(self):
        self.assertEqual(self.player.entity, self.hero)
        self.assertEqual(self.player.name, 'player_1')

    def test_set_position(self):
        self.player.set_position([10, 10])
        self.assertEqual(self.player.position, [10, 10])


class TestGameClass(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Arthas', 2000, 'Lich King')
        self.orc = Orc('Hellscream', 2000, 1.5)
        self.player = Player('player_1', self.hero)
        self.game = Game()

    def test_set_player(self):
        self.assertTrue(self.game.set_player('player_1', self.hero))
        self.assertFalse(self.game.set_player('player_1', self.orc))
        self.assertFalse(self.game.set_player('player_2', self.hero))
        self.assertTrue(self.game.set_player('player_2', self.orc))
        self.assertEqual(self.game.player_1.name, 'player_1')
        self.assertEqual(self.game.player_1.entity, self.hero)
        self.assertEqual(self.game.player_2.name, 'player_2')
        self.assertEqual(self.game.player_2.entity, self.orc)


if __name__ == "__main__":
    unittest.main()
