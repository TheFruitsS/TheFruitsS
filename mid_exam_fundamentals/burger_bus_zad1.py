number_of_cities = int(input())
name_of_city = (input())
earned_money = float(input())
owner_expenses = float(input())
total_profit = 0
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for number in range(number_of_cities):
    print(f"In {name_of_city} Burger Bus earned {total_profit} leva.")
    earned_money += earned_money - owner_expenses
    if number_of_cities == 3:
        owner_expenses += owner_expenses * 0.5
        print(f"In {name_of_city} Burger Bus earned {total_profit} leva.")
    if number_of_cities == 5:
        earned_money -= earned_money * 0.1

print(f"In {name_of_city} Burger Bus earned {total_profit} leva.")