import theatre_data


class ReservationSystem:
    def __init__(self, name):
        self.database = theatre_data.database
        self.cursor = self.database.cursor()

    def show_movies(self):
        movies = self.cursor.execute('''SELECT * FROM movies''')
        output = ''
        for row in movies:
            output += '[{0}]-{1} ({3})\n'.format(
                row['id'],
                row['name'],
                row['rating'])

    def show_projections(self, movie_id, date=None):
        projections = self.cursor.execute(
            '''SELECT
            movie.name,
            projections.id,
            projections.projection_date,
            projections.time,
            projections.type
            FROM movies projections
            ON movies.id = projections.movie_id
            WHERE movies.id = ?''', movie_id
            )

        print('Projections for {}'.format(movie_name))
        for row in projections:
            return('[{0}]-{1} {2} ({3})').format(
                row['id'],
                row['projection_date'],
                row['time'],
                row['type']
                )

    def get_movie_id(self):
        return input('movie id>')

    def make_reservation(self):
        self.show_movies()
        movie_id = self.get_movie_id()
        show_movie_projections(movie_id)