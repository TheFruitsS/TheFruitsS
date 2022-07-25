
#string = input()
#n = int(input())
#repeat_string = lambda a,b:a*b
#result = repeat_string(string, n)
#print(result)

def repeat_string(a, b):
    return str(a) * int(b)
string = input()
number = int(input())
print((repeat_string(string, number)))