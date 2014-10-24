

class Song:
    def __init__(self, name, artist, album, length, bitrate):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = length
        self.bitrate = bitrate

    def rate(self, value):
        if value < 0 or value > 5:
            raise ValueError

        self.rating = value
