num = input().split()

print(f'The minimum number is {min(num, key=int)}')
print(f'The maximum number is {max(num, key=int)}')
print(f'The sum number is: {sum(map(int, num))}')
