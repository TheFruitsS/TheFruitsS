start_interval = int(input())
final_interval = int(input())
special_num = int(input())
combination_counter = 0
flag = False
for num1 in range(start_interval, final_interval + 1):
    for num2 in range(start_interval, final_interval + 1):
        combination_counter += 1

        if num1 + num2 == special_num:
            print(f"Combination N:{combination_counter}({num1}+{num2}={special_num})")
            flag = True
            break

    if flag:
        break
if not flag:
    print(f'Nothing found')