import unittest
from song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('baba', 'Baba', 'Dqdo', 5, 400, 2)

    def test_init_(self):
        self.assertEqual(self.song.title, 'baba')
        self.assertEqual(self.song.artist, 'Baba')
        self.assertEqual(self.song.album, 'Dqdo')
        self.assertEqual(self.song.length, 400)
        self.assertEqual(self.song.rating, 5)
        self.assertEqual(self.song.bitrate, 2)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)
        with self.assertRaises(ValueError):
            self.song.rate(6)
        with self.assertRaises(ValueError):
            self.song.rate(-1)
        with self.assertRaises(ValueError):
            self.song.rate(3.5)

    def test_str_method(self):
        self.assertEqual(str(self.song), 'baba-Baba-Dqdo-400-5')


if __name__ == "__main__":
    unittest.main()
