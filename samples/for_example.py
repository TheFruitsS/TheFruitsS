k = int(input())
i = 0
j = 0
sabirane = 0
umnojenie = 0
for i in range(0, 9):

    for j in range(9, i):
        sabirane += i + j
        umnojenie += i * j
        if sabirane == umnojenie and k % 3 == 3:

            print(i, j)
