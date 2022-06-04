#От конзолата се прочитат 4 числа:
#•	На първия ред: цена на една видео карта – цяло число в интервала [1 … 2000]
#•	На втория ред: цена на един преходник – цяло число в интервала [1 … 50]
#•	На третия ред: цена на консумирания ток от карта за ден – реално число в интервала [0.01 ... 10.00]
#    • На четвъртия ред: печалба от една карта за един ден – реално число в интервала [1.00 ... 100.00]
from math import ceil

price_per_one_video_card = int(input())
price_per_one_convertor = int(input())
price_per_electric_per_day = float(input())
profit_from_one_video_card_per_day = float(input())

total_card_price = price_per_one_video_card * 13
total_convertor_price = price_per_one_convertor * 13
total_spend_money = total_card_price + total_convertor_price + 1000
profit_from_card_per_day = profit_from_one_video_card_per_day - price_per_electric_per_day
total_profit_per_day = 13 * profit_from_card_per_day
days_for_return = total_spend_money / total_profit_per_day

print(total_spend_money)
print(ceil(days_for_return))

