def astronaut_prob2():
    import re
    
    data = input()
    foods_pattern1 = r'\#([A-Za-z\sA-za-z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#'
    foods_pattern2 = r'\|([A-Za-z\sA-za-z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
    result_food1 = re.findall(foods_pattern1, data)
    result_food2 = re.findall(foods_pattern2, data)
    result_food1_list = [list(x) for x in result_food1]
    # list with lists
    result_food2_list = [list(x) for x in result_food2]
    # list with lists
    result_food = result_food1_list + result_food2_list
    # result list with lists
    days = 0

    if result_food1 or result_food2:

        calories_list = 0

        for currentlist in result_food:

            if int(currentlist[2]) > 10000:
                pass

            else:
                calories_list += int(currentlist[2])


        days = calories_list // 2000
        print(f"You have food to last you for: {days} days!")
        for food, best_before, calories in result_food:
            food_dict = {food: [best_before, calories]}
            if int(food_dict[food][1]) > 10000:
                del food_dict[food]

            else:
                print(f"Item: {food}, Best before: {food_dict[food][0]}, Nutrition: {food_dict[food][1]}")
    else:
        print(f"You have food to last you for: {days} days!")


astronaut_prob2()



