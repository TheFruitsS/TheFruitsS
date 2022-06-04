kids = 0
adults = 0
toys = 0
sweaters = 0
count_kids = 0
count_adults = 0
condition = False
count_toys = 0
count_sweaters = 0
age = input()
while True:
    if age == 'Christmas':
        break

    age = input()
    if age <= '16':
        kids = 1
        toys = 5

    count_kids += kids
    count_toys += toys

    if age > '16':
        adults = 1
        sweaters = 15

    count_sweaters = sweaters
    count_adults = adults

print(f'Number of adults: {count_adults}')
print(f'Number of kids: {count_kids}')
print(f'Money for toys: {count_toys}')
print(f'Money for sweaters:{count_sweaters}')
