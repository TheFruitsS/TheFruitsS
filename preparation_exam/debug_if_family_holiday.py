budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra_cost = int(input())

if nights > 7:
    price_per_night -= price_per_night * 0.05

cost = nights * price_per_night
additional_costs = budget * (percent_extra_cost / 100)
total_sum = cost + additional_costs

diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
# дебъгъра работи като се поставят брейкпойнтове където искаш да спре и да провери,ако не поставиш брейкпойнтове все едно
# рънваш кода без да ти изкарва никаква информация за това какво се случва в брейкпойнтовете а то дава и какво се случва във
# входа и там стойностите ги дава как се променят ако има труе