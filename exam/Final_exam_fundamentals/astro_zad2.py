def astronaut_prob2():
    import re

    data = input()
    foods_str = r'[#][A-z]+[#]\d+[\/]\d+[\/]\d+[#]\d+[#]|[|][A-z]+[|]\d+[\/]\d+[\/]\d+[|]\d+[|]'
    result_food = re.findall(foods_str, data).__str__()
    result_food_list_pattern = r'[#][A-z]+[#]|[|][A-z]+[|]'
    result_food_list = re.findall(result_food_list_pattern, result_food).__str__()
    food_pattern = r'\b[A-z]+'
    food = re.findall(food_pattern, result_food_list)

    data_patter = r'\d+[\/]\d+[\/]\d+'
    best_before = re.findall(data_patter, data)
    nutrition_pattern = r'[#]\d+[\/]\d+[\/]\d+[#]\d+[#]|\d+[\/]\d+[\/]\d+[|]\d+[|]'
    nutrition_str = re.findall(nutrition_pattern, data).__str__()

    nutrition_digits_pattern = r'[#]\d+[#]|[|]\d+[|]'
    nutrition_digits_list = re.findall(nutrition_digits_pattern, nutrition_str).__str__()
    cal_pattern = r'\d+'
    calories = re.findall(cal_pattern, nutrition_digits_list)

    calories_food = sum(list(map(int, calories)))

    astrounaut_food = {food[i]: [best_before[i], calories[i]] for i in range(0, len(best_before))}
    if calories_food > 2000:
        days = calories_food // 2000
        print(f'You have food to last you for: {days} days!')
        for key,value_best_before,value1_nutrition_dict in astrounaut_food:
            value_best_before = astrounaut_food[food][0]
            value1_nutrition_dict = astrounaut_food[food][1]
            print(f"Item: {key}, Best before:{value_best_before} , Nutrition:{value1_nutrition_dict} ")
    else:
        print(f'You have food to last you for: 0 days!')


astronaut_prob2()
