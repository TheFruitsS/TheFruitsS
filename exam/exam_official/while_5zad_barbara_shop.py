
target = int(input())
product_price = 0


while True:

    name_of_service = input()

    if 1 < target <= 5000:
        pass
    profit = product_price
    if profit >= target:
        print(f'You have reached your target for the day!\nEarned money: {profit}lv. ')
        break

    if name_of_service == 'closed':
        if profit < target:
            needed_money = target - profit
            print(f'Target not reached! You need {needed_money:.2f}lv. more.\nEarned money: {profit}lv!')
            break
        if profit > target:
            print(f'You have reached your target for the day!\nEarned money: {profit}lv. ')
            break

    if name_of_service == 'haircut':
        pass

    if name_of_service == 'mens':
        product_price += 15
    if name_of_service == 'ladies':
        product_price += 20
    if name_of_service == 'kids':
        product_price += 10
    if name_of_service == 'color':
        pass
    if name_of_service == 'touch up':
        product_price += 20
    if name_of_service == 'full':
        product_price += 30







