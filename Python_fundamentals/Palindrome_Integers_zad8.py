numbers = (list(map(str, input().split(', '))))
for num in numbers:
    print(list(reversed(num)) == list(num))

