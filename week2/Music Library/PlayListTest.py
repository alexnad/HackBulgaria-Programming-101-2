import unittest
from PlayList import PlayList
from song import Song


class TestPlayList(unittest.TestCase):
    def setUp(self):
        self.song1 = Song('baba', 'Baba', 'Dqdo', 5, 400, 2)
        self.song2 = Song('baba', 'BBaba', 'Dqdo', 5, 400, 2)
        self.song3 = Song('dqdo', 'Baaba', 'Dqdo', 5, 400, 2)

        self.play_list = PlayList()

    def test_add_song(self):
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)

        self.assertEqual(self.play_list[0], self.song1)
        self.assertEqual(self.play_list[1], self.song2)

    def test_remove_song(self):
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)
        self.play_list.add_song(self.song3)

        self.play_list.remove_song('baba')
        self.assertEqual(self.play_list[0], self.song3)

    def test_total_length(self):
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)
        self.play_list.add_song(self.song3)
        self.assertEqual(self.play_list.total_length(), 1200)

    def test_remove_disrated(self):
        song = Song('bab', 'dqdo', 'Dqdo', 3, 200, 5)
        self.play_list.add_song(song)
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)
        self.play_list.add_song(self.song3)

        with self.assertRaises(ValueError):
            self.play_list.remove_disrated(6)
        with self.assertRaises(ValueError):
            self.play_list.remove_disrated(-1)

        self.play_list.remove_disrated(3)
        self.assertEqual(self.play_list[0], self.song1)

    def test_remove_bad_quality(self):
        song = Song('bab', 'dqdo', 'Dqdo', 3, 200, 5)
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)
        self.play_list.add_song(self.song3)
        self.play_list.add_song(song)

        self.play_list.remove_bad_quality()
        self.assertEqual(self.play_list[0], song)

    def test_str_method(self):
        self.play_list.add_song(self.song1)
        self.play_list.add_song(self.song2)

        self.assertEqual(str(self.play_list), 'baba-Baba-Dqdo-400-5\nbaba-BBaba-Dqdo-400-5')


if __name__ == "__main__":
    unittest.main()
