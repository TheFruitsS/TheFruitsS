def astronaut_prob2():
    import re

    data = input()
    foods_pattern1 = r'\#[A-Za-z\sA-za-z]+\#\d{2}\/\d{2}\/\d{2}\#\d+\#|\|[A-Za-z\sA-za-z]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|'
    result_food1 = re.findall(foods_pattern1, data)

    days = 0
    if result_food1:
        txtli = [((x.replace('#', ',').replace('|', ','))[1:-1]).split(',')
                 for x in result_food1]

        calories = 0
        days = 0
        for food, best, cal in txtli:
            calories += int(cal)
            days = calories // 2000
        print(f"You have food to last you for: {days} days!")
        for food, best_before, calories in txtli:
            print(f"Item: {food}, Best before: {best_before}, Nutrition: {calories}")
    else:
        print(f"You have food to last you for: {days} days!")


astronaut_prob2()



