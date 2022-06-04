kids = 0
adults = 0
toys = 0
sweaters = 0
count_kids = 0
count_adults = 0
count_toys = 0
count_sweaters = 0

while True:
    age = input()
    if age == 'Christmas':
        break

    if int(age) <= 16:
        kids = 1
        toys = 5
        count_kids += kids
        count_toys += toys
    if int(age) > 16:
        adults = 1
        sweaters = 15
        count_adults += adults
        count_sweaters += sweaters


print(f'Number of adults: {count_adults}\nNumber of kids: {count_kids}\nMoney for toys: {count_toys}\nMoney '
      f'for sweaters:{count_sweaters}')
# when we have input int float and string then int(age) float(age) take input like a string