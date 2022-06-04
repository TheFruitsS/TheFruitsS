film_name = input()
days = int(input())
tickets = int(input())
tickets_price = float(input())
cinema = int(input())

price_for_tickets_per_day = tickets * tickets_price
total_profit = price_for_tickets_per_day * days
total_profit -= total_profit * (cinema / 100)
print(f'The profit from the movie {film_name} is {total_profit:.2f} lv.')
