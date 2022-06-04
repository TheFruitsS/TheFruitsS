n = int(input())
i = int()
j = int()
for i in range(1, 10):

    for j in (9, i):
        if i + j == i * j and n % 5 == 0:
            print(i, j)
            break

    break
print(i, j)
