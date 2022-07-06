number = int(input())
wagons = [0]*number
#when we create list with [0] and * number => if number = 5 > [0, 0, 0, 0, 0]
while True:
    command = input()
    if command == 'End':
        break

    data = command.split(' ')
    current_command = data[0]

    if current_command == 'add':
        people_to_add = data[1]
        wagons[-1] += int(people_to_add)
    elif current_command == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people
    elif current_command == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people
print(wagons)