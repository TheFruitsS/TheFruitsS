import sys

movies = int(input())
low_rating = sys.maxsize
low_movie_name = ''
max_rating = 0
max_movie_name = ''
sum_of_rating = 0

for count in range(movies):
    name_of_movie = input()
    rating_of_movie = float(input())
    sum_of_rating += rating_of_movie

    if rating_of_movie > max_rating:
        max_rating = rating_of_movie
        max_movie_name = movies

    if rating_of_movie < low_rating:
        low_movie_name = rating_of_movie
        low_movie_name = movies

average_rating = sum_of_rating / movies
print(f'{max_movie_name} is with highest rating: {max_rating:.1f}')
print(f'{low_movie_name} is with lowest rating: {low_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')



