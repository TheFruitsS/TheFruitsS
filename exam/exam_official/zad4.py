N = int(input())
M = int(input())
S = int(input())

for x in reversed(range(N, M+1)):
    if x % 2 ==0 and x % 3 ==0 :
        if x == S:
            break
        print(x, end=' ')