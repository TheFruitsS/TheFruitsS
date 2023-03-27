from collections import deque

seats = input().split(', ')
first_seats = deque(int(x) for x in input().split(', '))
seconds_seats = deque(int(x) for x in input().split(', '))

taken_seats = []

rotations = 0

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1

    first_num = first_seats.popleft()
    seconds_num = seconds_seats.pop()

    letter = chr(first_num + seconds_num)
    first_opt = str(first_num) + letter
    second_option = str(seconds_num) + letter
    if first_opt in taken_seats or second_option in taken_seats:
        continue
    if first_opt in seats:
        taken_seats.append(first_opt)
        continue
    if second_option in seats:
        taken_seats.append(second_option)
        continue

    first_seats.append(first_num)
    seconds_seats.appendleft(seconds_num)
print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")