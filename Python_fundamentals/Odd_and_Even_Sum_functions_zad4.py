num = input()
x = [int(a) for a in str(num)]
even_nos = [num for num in x if num % 2 == 0]
odd_num = [num for num in x if num % 2 != 0]

print(f'Odd sum = {(sum(odd_num))}, Even sum = {(sum(even_nos))}')