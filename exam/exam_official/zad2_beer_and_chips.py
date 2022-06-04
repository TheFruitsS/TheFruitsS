#От конзолата се четат 4 реда:
#  • На първия ред - името на футболният фен – текст
#   • На втория ред - предвиденият бюджет  – реално число в диапазона [1.0… 100 000.0]
#   • На третия ред - брой бутилки бира – цяло число в диапазона [1… 100 000]
#   • На четвърти ред - брой пакети чипс – цяло число в диапазона [1… 100 000]
from math import ceil

football_fen = input()
budget = float(input())
bottle_of_beer = int(input())
pack_of_chips = int(input())

total_price_per_beer = 1.20 * bottle_of_beer
price_per_one_pack_chips = 0.45 * total_price_per_beer
total_price_per_chips = price_per_one_pack_chips * pack_of_chips
total_price_per_chips = ceil(total_price_per_chips)
total_sum = total_price_per_beer + total_price_per_chips
left_money = budget - total_sum

diff = abs(budget - total_sum)
if total_sum <= budget:
    print(f'{football_fen} bought a snack and has {left_money:.2f} leva left.')


elif total_sum >= budget:
    print(f'{football_fen} needs {diff:.2f} more leva!')


