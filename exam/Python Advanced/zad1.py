from collections import deque

times = deque(map(int, input().split(" ")))
tasks = deque(map(int, input().split(" ")))

dart = 0
sec = 0
third = 0
fourth = 0
print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
while True:
    if not times:
        break
    if not tasks:
        break
    current_time = times[0]
    current_task = tasks[-1]
    duck = current_task * current_time


    if duck < 60:
        times.popleft()
        tasks.pop()
        dart += 1

    if duck > 60:
        tasks.pop()
        tasks.append(current_task - 2)


    if 61 < duck < 120:
        times.popleft()
        tasks.pop()
        sec += 1
    if 61 > duck > 120:
        tasks.pop()
        tasks.append(current_task - 2)


    if 121 < duck < 180:
        times.popleft()
        tasks.pop()
        third += 1
    if 121 > duck > 180:
        tasks.pop()
        tasks.append(current_task - 2)



    if 181 < duck < 240:
        times.popleft()
        tasks.pop()
        fourth += 1
    if 181 > duck > 240:
        tasks.pop()
        tasks.append(current_task - 2)

print(f'Darth Vader Ducky: {dart}')
print(f'Thor Ducky: {sec}')
print(f'Big Blue Rubber Ducky: {third}')
print(f'Small Yellow Rubber Ducky: {fourth}')