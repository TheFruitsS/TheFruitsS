num = int(input())
for first_num in range(0, num):
    for second_num in range(0, num):
        for third_num in range(0, num):
            print(f"{chr( 97+ first_num)}{chr (97 + second_num) }{ chr (97 + third_num)}")
