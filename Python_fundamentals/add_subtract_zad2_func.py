def sum_numbers(first, second):
    return first + second
def subtract(sum, third_number):
    return sum - third_number
def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second_integers, third)
    return result
#Important every functions have their own parameters def sum numbers (first and second) is not the same as the others they have another first and seconds parameters
first_numbers = int(input())
second_numbers = int(input())
third_number = int(input())
print(add_and_subtract(first_numbers, second_numbers,third_number))