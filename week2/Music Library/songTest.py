import unittest
from song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('baba', 'Baba', 'Dqdo', 400, 2)

    def test_init_(self):
        self.assertEqual(self.song.name, 'baba')
        self.assertEqual(self.song.artist, 'Baba')
        self.assertEqual(self.song.album, 'Dqdo')
        self.assertEqual(self.song.length, 400)
        self.assertEqual(self.song.bitrate, 2)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)
        with self.assertRaises(ValueError):
            self.song.rate(6)



if __name__ == "__main__":
    unittest.main()
