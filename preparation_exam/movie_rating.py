movies = int(input())
if not 1 <= movies <= 20:
    raise Exception("Wrong Input")


movies_list = []
rating_list = []

for count in range(0, movies):
    name_of_movie = input()
    rating_of_movie = float(input())
    if not 1 <= rating_of_movie <= 10:
        raise Exception("Wrong Input")
    movies_list.append(name_of_movie)
    rating_list.append(rating_of_movie)
highest_rating = max(rating_list)
lowest_rating = min(rating_list)
average = sum(rating_list) / movies

print(f'{movies_list[rating_list.index(highest_rating)]} is with highest rating: {highest_rating:.1f}')
print(f'{movies_list[rating_list.index(lowest_rating)]} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average:.1f}')



