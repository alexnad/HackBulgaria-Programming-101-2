import data


class Cinema:
    def __init__(self):
        self.session = data.session

    def correct_movie_info(self):
        return True

    def add_movie(self, movie):
        if self.correct_movie_info(movie):
            movie = data.Movie(**movie)
            self.session.add(movie)
            return 'Movie succefuly added!'
        return 'Error! Invalid arguments!'

    def add_reservation(self, reservation):
        if self.correct_reservation_info(reservation):
            reserv = data.Reservation(**reservation)
