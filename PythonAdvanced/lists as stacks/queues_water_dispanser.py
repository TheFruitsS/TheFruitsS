from collections import deque

queue = deque()
water_quantity = int(input())

while True:
    name = input()
    if name == 'Start':
        break
    queue.append(name) # add people to queue

command = input()
while command != "End":

    if "refill" in command:
        liters = command.split()
        if len(liters) == 2:
            water_quantity += int(liters[1])
                # increase liters

    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f"{water_quantity} liters left")