chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
veg_menu_price = veg_menu * 8.15
delivery_price = 2.50

final_sum_menu = chicken_menu_price + fish_menu_price + veg_menu_price

dessert_price = final_sum_menu * 0.2


final_price_order = final_sum_menu + dessert_price + delivery_price

print(final_price_order)
