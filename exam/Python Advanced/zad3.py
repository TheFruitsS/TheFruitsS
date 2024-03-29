import os
def movie_organizer(*movie_tuple):

    movie_dict = dict(movie_tuple)
    movies = []

    for movie in movie_dict.keys():
        movies.append(movie)

    genres = []
    genres.sort()

    for genre in movie_dict.values():
        genres.append(genre)

    result1 = {genre1:genres.count(genre1) for genre1 in genres}
    counts = []
    counts.sort()
    for x in result1.values():
        counts.append(x)
    result = {movie: [genres.count(movie), movie_dict.keys()] for movie in genres}
    for x,y in sorted(result1.items()):
        print(f'{x} - {y}')
        for movie in sorted(movie_dict.keys()):
            print(movie)






print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))