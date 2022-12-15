def astronaut_prob2():
    import re
    
    data = input()
    foods_pattern = r'[\#\|]([A-Z\sa-z]+)[\#\|](\d{2}\/\d{2}\/\d{2})[\#\|](\d+)[\#\|]'
    result_food = re.findall(foods_pattern, data)

    if result_food:

        calories_list = 0

        for food, best_before, calories in result_food:
            food_dict = {food: [best_before, calories]}
            calories_list += int(food_dict[food][1])

        if calories_list > 2000:
            days = calories_list // 2000
            print(f"You have food to last you for: {days} days!")
            for food, best_before, calories in result_food:
                food_dict = {food: [best_before, calories]}
                print(f"Item: {food}, Best before: {food_dict[food][0]}, Nutrition: {food_dict[food][1]}")
        else:
            print("You have food to last you for: 0 days!")
 

astronaut_prob2()
