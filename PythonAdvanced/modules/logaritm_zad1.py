from math import log, e
'''ternary operator'''
number = int(input())
base_input = input()
base = e if base_input == 'natural' else int(base_input) #in one variable we define if
#https://www.educative.io/answers/what-is-the-ternary-operator-in-python
print(log(number, base))