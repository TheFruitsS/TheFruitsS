flag = False

for hour in range(0, 24):
    for minutes in range(0, 60):
        if minutes == 5:
            flag = True
            break
        print(f'{hour}:{minutes}')

    if flag:
        break
