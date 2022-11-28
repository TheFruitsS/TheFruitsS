n = int(input())
combinations = 0
combination = 0
comb = 0
a = 0
b = 0
c = 0
d = 0

sum = 0
proizv = 0

condition = False

for a in range(0, 10):
    for b in range(10, a):
        for c in range(0, 10):
            for d in range(10, c):
                if sum == proizv and n % 5 == 5:
                    combinations = a + b + c + d
                    combination = a * b * c * d
                    comb += 1
                    if proizv / sum == 3 and n % 3 == 0:
                        combinations = a + b + c + d
                        #combination = a * b * c * d
                        #comb += 1

print(comb)