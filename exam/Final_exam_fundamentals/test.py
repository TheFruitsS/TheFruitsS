

movie = []
movies = []
ticket = 0
while True:
    command = input()

    movie.append(command)
    movies.append(command)
    tickets = 0
    kid = movie.count('kid')
    standard = movie.count('standard')
    student = movie.count('student')

    if command == 'Finish':
        break

    if 0 < command.isdigit() < 100:
        ticket = int(command)

    if (kid + standard + student) / ticket * 100 >= 100:
        movie.clear()

    if command == 'End':

        tickets += int(movie[1])

        seats_movie = (kid + standard + student) / ticket * 100
        print(f'{movie[0]} - {seats_movie:.2f}% full.')
        movie.clear()

try:
    tickets += int(movie[1])
    seats_movie = (kid + standard + student) / tickets * 100
    total_tickets = movies.count('kid') + movies.count('standard') + movies.count('student')
    students = movies.count('student') / total_tickets * 100
    kids = movies.count('kid') / total_tickets * 100
    standarts = movies.count('standard') / total_tickets * 100

    print(f'{movie[0]} - {seats_movie:.2f}% full.')
    print(f'Total tickets: {total_tickets}')
    print(f'{students:.2f}% student tickets.')
    print(f'{standarts:.2f}% standard tickets.')
    print(f'{kids:.2f}% kids tickets.')

except ZeroDivisionError:
    print('Error')