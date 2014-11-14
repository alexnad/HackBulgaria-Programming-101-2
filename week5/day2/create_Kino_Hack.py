import theatre_data


def main():
    movies = [
        ('The Hunger Games: Catching Fire', 7.9),
        ('Weck-It Ralph', 7.8),
        ('Her', 8.3)
    ]
    database = theatre_data.database('HackBulgaria')
    for movie in movies:
        theatre_data.add_movie(movie, database)

    projections = [
        (1, '3D', '2014-04-01', '19:10'),
        (1, '2D', '2014-04-01', '19:00'),
        (1, '4DX', '2014-04-02', '21:00'),
        (3, '2D', '2014-04-05', '20:20'),
        (2, '3D', '2014-04-02', '22:00'),
        (2, '2D', '2014-04-02', '19:30')
    ]
    for projection in projections:
        theatre_data.add_projection(projection, database)

if __name__ == "__main__":
    main()
