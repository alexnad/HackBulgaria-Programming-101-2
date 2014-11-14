import sqlite3


def database(theatre_name):
    theatre_name += '.db'
    database = sqlite3.connect(theatre_name)
    database.row_factory = sqlite3.Row
    cursor = database.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY,
            name TEXT unique,
            rating REAL
            )
        ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS projections(
            id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            type TEXT,
            projection_date TEXT,
            time TEXT unique,
            FOREIGN KEY(movie_id) REFERENCES movies(id)
            )
        ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(
            id INTEGER PRIMARY KEY,
            projection_id INTEGER,
            name TEXT,
            row INTEGER,
            column INTEGER,
            FOREIGN KEY(projection_id) REFERENCES projections(id)
            )
        ''')

    return database


def add_movie(movie, cursor, database):
    cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''', movie)
    database.commit()
    return 'Movie added'


def remove_movie(id, cursor, database):
    cursor.execute('''DELETE FROM movies WHERE id = ?''', id)
    cursor.execute('''DELETE FROM projections WHERE movie_id = ?''', id)
    database.commit()
    return 'Movie removed'


def add_projection(projection, cursor, database):
    cursor.execute('''INSERT INTO
        projections(movie_id, type, projection_date, time)
        VALUES(?,?,?,?)''', projection)

    database.commit()
    return 'Projection added'


def remove_projection(projection_id, cursor, database):
    cursor.execute('''DELETE FROM projections WHERE id=?''', projection_id)
    database.commit()
    return 'Projection removed'


def add_reservation(reservation, cursor, database):
    cursor.execute('''INSERT INTO
        reservations(name, projection_id, row, column)
        VALUES(?,?,?,?)''')

    database.commit()
    return 'Reservations succesfuly added'


def remove_reservarion(reservation_id, cursor, database):
    cursor.execute('''DELETE FROM reservations WHERE name = ?''',
                  (reservation_id,))

    database.commit()
    return 'Reservation removed'
