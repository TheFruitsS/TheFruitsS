def calculation_ticket(ticket, tickets):
    return f'{ticket / tickets * 100:.2f}'


standard, student, kid = 0, 0, 0

while True:
    movie = input()

    if movie == 'Finish':
        break

    free_seats = int(input())
    sold_tickets = 0

    while sold_tickets < free_seats:
        ticket = input()
        if ticket == 'End':
            break

        if ticket == 'standard':
            standard += 1
        elif ticket == 'student':
            student += 1
        elif ticket == 'kid':
            kid += 1
        sold_tickets += 1

    print(f"{movie} - {sold_tickets / free_seats * 100:.2f}% full.")

total_tickets = standard + student + kid

print(f"Total tickets: {total_tickets}")
print(f"{calculation_ticket(student,total_tickets)}% student tickets.")
print(f"{calculation_ticket(standard,total_tickets)}% standard tickets.")
print(f"{calculation_ticket(kid,total_tickets)}% kids tickets.")