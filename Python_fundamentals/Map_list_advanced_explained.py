'''def square_numbers(n):
    return n ** 2
print(list(map(square_numbers, [1, 2, 3, 4, 5])))'''
#map has (function, iterable)

strings_list = ["1","2","3","4"]
numbers_list = list(map(int, strings_list))
print(numbers_list)