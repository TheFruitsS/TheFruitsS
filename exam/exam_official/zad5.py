bought_food = int(input()) * 1000
counter = 0
while True:
    command = input()
    if command == 'Adopted':
        break
    if command.isdigit():
        counter += int(command)

if bought_food >= counter:
    print(f"Food is enough! Leftovers: {bought_food - counter} grams.")
if counter > bought_food:
    print(f"Food is not enough. You need {counter - bought_food} grams more.")