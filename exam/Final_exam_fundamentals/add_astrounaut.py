import re

def astronaut_prob2():

    data = input()
    foods_str = r'[A-z]+[a-z]+'
    result_food = re.finditer(foods_str, data)
    data_patter = r'\d+[\/]\d+[\/]\d+'
    best_before = re.finditer(data_patter, data)
    nutrition_pattern = r'[|]\d+[|]'
    nutrition_str = re.finditer(nutrition_pattern, data)
    astrounaut_food = {}
    every_single_food = str
    astrounaut_food[every_single_food]
    values = []


    for food in result_food:
        every_single_food = food.group()

        #print(every_single_food)
    for data_exp in best_before:
        data_of_expiration = data_exp.group()
        values.append(data_of_expiration)
        #print(data_of_expiration)
    for nutrition in nutrition_str:
        energy_calories = nutrition.group()
        values.append(energy_calories)
        #print(energy_calories)

    print(astrounaut_food)


astronaut_prob2()