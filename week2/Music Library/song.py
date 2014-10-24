

class Song:
    MAX_RATING = 5
    MIN_RATING = 0

    def __init__(self, name, artist, album, rating, length, bitrate):
        self.name = name
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def __str__(self):
        return '{0}-{1}-{2}-{3}-{4}'.format(self.name, self.artist, self.album, self.length, self.rating)

    def rate(self, value):
        value_in_limits = value < Song.MIN_RATING or value > Song.MAX_RATING
        if value_in_limits or isinstance(value, float):
            message = 'Error! Value must be an integer between {} and {}'
            raise ValueError(message.format(Song.MIN_RATING, Song.MAX_RATING))

        self.rating = value
