def calculation_func(number_a, number_b, operation):
    if operation == 'multiply':
        return number_a * number_b
    elif operation == 'divide':
        return int(number_a / number_b)
    elif operation == 'add':
        return number_a + number_b
    elif operation == 'subtract':
        return number_a / number_b
type_of_operation = input()
first_numbers = int(input())
second_numbers = int(input())
print(calculation_func(first_numbers, second_numbers, type_of_operation))