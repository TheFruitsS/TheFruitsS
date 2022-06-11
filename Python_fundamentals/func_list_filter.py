numbers = [1, 2, 3, 4, 5, 6, 10, 11, 13]

def check_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = list(filter(check_numbers, numbers))

print(result)