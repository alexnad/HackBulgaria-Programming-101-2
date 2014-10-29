from song import Song
import json


class PlayList:
    LOW_BITRATE = 4

    def __init__(self, name='new_playlist'):
        self.name = name
        self.songs = []

    def __getitem__(self, song_index):
        return self.songs[song_index]

    def __str__(self):
        return '\n'.join([str(song) for song in self.songs])

    def change_playlist_title(self, title):
        self.title = title

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_title):
        self.songs = [song for song in self.songs if song.title != song_title]

    def total_length(self):
        return sum([song.length for song in self.songs])

    def remove_disrated(self, rating):
        not_valid_rating = rating > Song.MAX_RATING or rating < Song.MIN_RATING
        if not_valid_rating or isinstance(rating, float):
            raise ValueError
        self.songs = [song for song in self.songs if song.rating >= 4]

    def remove_bad_quality(self):
        self.songs = [song for song in self.songs
                      if song.bitrate > PlayList.LOW_BITRATE]

    def save(self):
        songs = [{key: song.__dict__[key] for key in song.__dict__}
                 for song in self.songs]

        data = {'name': self.name, 'songs': songs}
        filename = self.name + '.txt'
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as infile:
            content = infile.read()
            play_list = json.loads(content)

        new_playlist = PlayList()
        new_playlist.songs = [Song(**song) for song in play_list['songs']]
        return new_playlist
