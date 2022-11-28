

models_computers = int(input())
possible_sells_1 = 0
possible_sells_2 = 0
possible_sells_3 = 0
possible_sells_4 = 0
possible_sells_5 = 0
possible_sells_6 = 0
rating = 0
rating_1 = 0
rating_2 = 0
rating_3 = 0
rating_4 = 0
rating_5 = 0
for count in range(models_computers):
    num = input()
    rating = float(num[len(num) - 1])
    sells = float(num[:2])
    if rating == 2:
        rating_1 += rating
        possible_sells_1 = 0
    if rating == 3:
        rating_2 += rating
        possible_sells_2 += sells * 0.5
    if rating == 4:
        rating_3 += rating
        possible_sells_3 += sells * 0.7
    if rating == 5:
        rating_4 += rating
        possible_sells_4 += sells * 0.85
    if rating == 6:
        possible_sells_5 += sells * 1
        rating_5 += rating

average_rating = (rating_1 + rating_2 + rating_3 + rating_4 + rating_5) / models_computers
possible_sells_main = possible_sells_1 + possible_sells_2 + possible_sells_3 + possible_sells_4 + possible_sells_5
print(f'{possible_sells_main:.2f}')
print(f'{average_rating:.2f}')
