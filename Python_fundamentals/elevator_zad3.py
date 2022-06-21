import math
number_of_people_N = int(input())
capacity_P = int(input())
#if capacity_P == 0:
    #print(0)

#elif ((number_of_people_N % capacity_P) % capacity_P) == 0:
    #print(math.floor(number_of_people_N / capacity_P))

#else:
   # courses = (number_of_people_N // capacity_P) + (capacity_P % (number_of_people_N % capacity_P))

   # if courses == 0:
      #  print(1)

  #  else:
      #  print(courses)
#return 60% success in judge system.I guess because I used a formula

courses = number_of_people_N / capacity_P
print(math.ceil(courses))
#return 100 percent in judge system