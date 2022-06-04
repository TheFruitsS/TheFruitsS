rolls_paper = int(input())
rolls_plat = int(input())
glue_liters = float(input())
discount = int(input())

price_rolls_paper = rolls_paper * 5.80
price_rolls_plat = rolls_plat * 7.20
price_glue_liters = glue_liters * 1.20
total_price = price_rolls_paper + price_rolls_plat + price_glue_liters
discount_price = total_price - discount / 100 * total_price

print(f'{discount_price:.3f}')
