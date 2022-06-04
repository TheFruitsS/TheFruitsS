Special_number = int(input())

for first_num in range(1, 10):
    for second_num in range(1, 10):
        for third_num in range(1, 10):
            for forth_num in range(1, 10):
                if Special_number % first_num == 0 and Special_number % second_num == 0 and \
                        Special_number % third_num == 0 and Special_number % forth_num == 0:
                    print(f'{first_num}{second_num}{third_num}{forth_num}', end=' ')
