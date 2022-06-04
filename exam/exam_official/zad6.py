kids = 0
adults = 0
toys = 0
sweaters = 0

count_adults = 0
count_kids = 0
count_toys = 0
count_sweaters = 0
world = ''
condition = False

while True:
    world = input()
    if world == 'Christmas':
        break
    age = input()
    toys = 5
    sweaters = 15
    toys += 1
    sweaters += 1

    if age <= '16':
        condition = True
        kids = age * toys
        toys = 5
        break

    if age > '16':
        condition = True
        adults = 1
        sweaters = 15
        break

    count_adults += adults
    count_kids += kids


print(f'Number of adults: {count_adults}')
print(f'Number of kids: {count_kids}')
print(f'Money for toys: {count_toys}')
print(f'Money for sweaters:{count_sweaters}')