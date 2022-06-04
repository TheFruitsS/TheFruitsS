target = float(input())
product_price = 0
budget_condition = False
needed_money = 0
profit = int()
while True:

    name_of_service = input()
    if name_of_service == 'closed':
        print(f'Target not reached! You need {needed_money:.2f}lv. more.\nEarned money:{profit:.2f} leva!')
        break
    vid = input()

    if name_of_service == 'haircut':
        if vid == 'mens':
            product_price = 15
        if vid == 'ladies':
            product_price = 20
        if vid == 'kids':
            product_price = 10
    if name_of_service == 'color':
        if vid == 'touch up':
            product_price = 20
        if vid == 'full color':
            product_price = 30
    profit += product_price
    needed_money = target - profit

    if profit >= target:
        print(f'You have reached your target for the day!\nEarned money  {profit:.2f} leva. ')
        break

if profit <= target:
    budget_condition = True

if not budget_condition:
    print(f'Target not reached! You need {needed_money:.2f}lv. more.\nEarned money:{profit:.2f} leva!')
# kogato iskame da sabere vsi4ko ot cikala go izkarvame izvan usloviqta no v cikala
