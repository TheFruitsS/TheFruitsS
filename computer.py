computers = int(input())
rating = 0
last_num = 0
other_num = 0
sells = 0

for count in range(computers):
    possible_sells_and_rating = int(input())

    if rating == '2':
        sells = 0
    if rating == '3':
        sells = computers * 0.5
    if rating == '4':
        sells = computers * 0.7
    if rating == '5':
        sells = computers * 0.85
    if rating == '6':
        sells = computers * 1
    if 2 <= float(rating) >= 6:
        rating = possible_sells_and_rating[len(possible_sells_and_rating) - 1]

sells = possible_sells_and_rating[:2]
print(f'{float(rating):.2f}')
print(f'{float(sells):.2f}')


