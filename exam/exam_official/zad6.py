locations = int(input())


for x in range(locations):

    average = int(input())
    days = int(input())
    counter  = 0

    for y in range(days):
        counter += int(input())
    average_day = counter / days
    if average_day >= average:
        print(f"Good job! Average gold per day: {average_day:.2f}.")
    if average_day < average:
        print(f"You need {(average - average_day):.2f} gold.")