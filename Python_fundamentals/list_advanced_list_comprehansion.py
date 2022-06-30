import timeit
'''checking time for performance of task'''
#time with comprehension is 0,48
#time with loop is 0.58
#def even_numbers_with_comprehension():
    #return [num for num in [1, 2, 3, 4, 5, 6]]
#def even_numbers_with_loop():
 #   even_nums = []
  #  for num in [1, 2, 3, 4, 5, 6]:
   #     even_nums.append(num)
    #return even_nums
#print(timeit.timeit(even_numbers_with_comprehension))
#print(timeit.timeit(even_numbers_with_loop))

#print(sum([num ** 2 for num in range(1000)]))
#comprehension is good to be used for not too large numbers because it will be very slow or not responding
#print(sum([num ** 2 for num in range(10000000000000)]))
#print([num for num in range(11)])
#print(list(range(11)))

#nums = [1,2,3,4,5,6,7,8,9,10]
#result = [num for num in nums if num % 2 == 0 if num > 5 if num != 10]
#print(result)

matrix = [[x for x in range(3)]for _ in range(3)]
print(matrix)