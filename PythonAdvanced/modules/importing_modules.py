from random import random
'''two different ways to import modules'''
my_list = random()
print(my_list)


import random

my_list = random.random()
print(my_list)


from random import random as randomed
'''when we want to change the name of the function we use as and the new name'''
my_list = randomed()
print(my_list)