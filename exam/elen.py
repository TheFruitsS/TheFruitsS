import math
from math import floor

days = int(input())
food_need = int(input())
food_first = float(input())
food_two = float(input())
food_three = float(input())

elen_one = days * food_first
elen_two = days * food_two
elen_three = days * food_three
total_food = elen_one + elen_two + elen_three
food_left = food_need - total_food
absolut_number = abs(food_left)

if total_food < food_need:
    print(math.floor(absolut_number), 'kilos of food left.', end='')

elif total_food > food_need:
    print(round(absolut_number), 'more kilos of food are needed.', end='')
