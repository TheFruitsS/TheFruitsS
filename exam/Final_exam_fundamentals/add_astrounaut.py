def astronaut_prob2():
    import re
    
    data = input()
    foods_pattern1 = r'\#[A-Za-z\sA-za-z]+\#\d{2}\/\d{2}\/\d{2}\#\d+\#|\|[A-Za-z\sA-za-z]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|'
    foods_pattern2 = r'[A-Za-z\sA-Za-z]+\b|[\d{2}\/\d{2}\/\d{2}]+|[\d]+'
    result_food1 = re.findall(foods_pattern1, data)
    #result_food2 = re.findall(foods_pattern2, result_food1)
    # ['Bread', '19/03/21', '4000', 'Apples', '08/10/20', '200', 'Carrots', '06/08/20', '500']
    #txt = ['apple,12/12/12,400','banana,11/12/21,500','cherry,10/10/10,550','orange,21/12/22,7000']# setting the maxsplit parameter to 1, will return a list with 2 elements!txtli = [x.split(',') for x in txt]fooddict = {}fooddict = {food: [best, cal]for food, best, cal in txtli if not int(cal) > 2000}print(fooddict)#print(txtli[1][2])
    txtli = [((x.replace('#', ',').replace('|', ','))[1:-1]).split(',') for x in result_food1]
    # replace str ch after that slicing first and last char snd after hat splitting to have list of lists for dict
    fooddict = {food: [best, cal] for food, best, cal in txtli if not int(cal) > 10000}
    #showing the right food if its more than 2000 cal is not valid
    print(fooddict)
    days = 0

    if result_food1:

        calories_list = sum(fooddict[2])




        days = calories_list // 2000
        print(f"You have food to last you for: {days} days!")
        for food, best_before, calories in result_food2:
            food_dict = {food: [best_before, calories]}
            if int(food_dict[food][1]) > 10000:
                del food_dict[food]

            else:
                print(f"Item: {food}, Best before: {food_dict[food][0]}, Nutrition: {food_dict[food][1]}")
    else:
        print(f"You have food to last you for: {days} days!")


astronaut_prob2()



#pattern = '\#[A-Za-z\sA-za-z]+\#\d{2}\/\d{2}\/\d{2}\#\d+\#|\|[A-Za-z\sA-za-z]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|'