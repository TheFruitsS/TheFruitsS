def factorial_calc(num):
    for factorial in range(1, num):
        num *= factorial
    return num
first_num = int(input())
sec_num = int(input())
first_num_factorial = factorial_calc(first_num)
sec_num_factorial = factorial_calc(sec_num)
result = first_num_factorial / sec_num_factorial


print(f'{result:.2f}')