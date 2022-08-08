def burger_bus(counts_city):
    total = 0
    my_list = ([])
    for city in range(1, counts_city + 1):

        town_of_visit = input()
        income = float(input())
        expenses = float(input())
        profit = income - expenses

        if city % 3 == 0:
            profit = income - expenses * 1.5

        if city % 5 == 0:
            profit = income * 0.9 - expenses

        total += profit
        my_list.append(f"In {town_of_visit} Burger Bus earned {profit:.2f} leva.")
    # printing every number from the list on new line
    print(*my_list, sep="\n")
    print(f"Burger Bus total profit: {total:.2f} leva.")
total_city = int(input())
burger_bus(total_city)
#functions can be with empty parametar () and everything to be in the body of the function
#parameters in this case in the for loop should be there because you cant declarated them in the function and loop