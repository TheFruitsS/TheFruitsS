water_tank_capacity = 255
times_of_pour = int(input())


sum_times = 0

for times_of_pour in range(times_of_pour):
    each_time = int(input())
    if water_tank_capacity - each_time < 0:
        print("Insufficient capacity!")
        continue
    sum_times += each_time
    water_tank_capacity -= each_time
print(sum_times)