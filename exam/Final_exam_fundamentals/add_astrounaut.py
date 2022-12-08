def additional_print_function(astronaut_dict):
    for key in astronaut_dict:
        value_best_before = astronaut_dict[key][0]
        value1_nutrition_dict = astronaut_dict[key][1]
        print(f"Item: {key}, Best before: {value_best_before}, Nutrition: {value1_nutrition_dict}")


def astronaut_prob2():
    import re

    data = input()
    foods_str = r'[#|][A-z]+\b\D+[A-z]+[#|]\d{2}/\d{2}/\d{2}[#|]\d+|[#|][A-z]+[#|]\d{2}/\d{2}/\d{2}[#|]\d+'
    result_food = re.findall(foods_str, data).__str__()

    food_pattern = r'\w+[A-z]\D+[A-z]'
    food = re.findall(food_pattern, result_food)


    data_pattern = r'\d{2}/\d{2}/\d{2}'
    best_before = re.findall(data_pattern, data)

    nutrition_pattern = r'[#|]\D+[#|]\d{2}/\d{2}/\d{2}[#|]'
    nutrition_str = re.split(nutrition_pattern, result_food).__str__()


    cal_pattern = r'\d+'
    calories = re.findall(cal_pattern, nutrition_str)

    calories_food = sum(list(map(int, calories)))

    astronaut_food = {food[i]: [best_before[i], calories[i]] for i in range(0, len(food))}
    if calories_food > 2000:
        days = calories_food // 2000
        print(f'You have food to last you for: {days} days!')
        additional_print_function(astronaut_food)
    else:
        print("You have food to last you for: 0 days!")



astronaut_prob2()