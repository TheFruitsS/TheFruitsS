kind = input()
count_pastry = int(input())
day = int(input())
if 1 <= count_pastry <= 10000:
    if kind == 'Cake':

        cakes = 0
        discount15 = 0
        discount25 = 0
        day_discount = 0
        total = 0

        if 0 < day <= 22:
            cakes += count_pastry * 24

            if 100 <= cakes <= 200:
                discount15 += cakes * 0.15
            if cakes > 200:
                discount25 += cakes * 0.25
            total += cakes - discount15 - discount25
            if day <= 15:
                day_discount += total * 0.1

            total_all = total - day_discount

            print(f'{total_all:.2f}')
        if 22 < day <= 24:
            cakes += count_pastry * 28.70
            print(f'{cakes:.2f}')

    if kind == 'Souffle':

        cakes = 0
        discount15 = 0
        discount25 = 0
        day_discount = 0
        total = 0

        if 0 < day <= 22:
            cakes += count_pastry * 6.66

            if 100 <= cakes <= 200:
                discount15 += cakes * 0.15
            if cakes > 200:
                discount25 += cakes * 0.25
            total += cakes - discount15 - discount25
            if day <= 15:
                day_discount += total * 0.1

            total_all = total - day_discount

            print(f'{total_all:.2f}')
        if 22 < day <= 24:
            cakes += count_pastry * 9.80
            print(f'{cakes:.2f}')

    if kind == 'Baklava':

        cakes = 0
        discount15 = 0
        discount25 = 0
        day_discount = 0
        total = 0

        if 0 < day <= 22:
            cakes += count_pastry * 12.60

            if 100 <= cakes <= 200:
                discount15 += cakes * 0.15
            if cakes > 200:
                discount25 += cakes * 0.25
            total += cakes - discount15 - discount25
            if day <= 15:
                day_discount += total * 0.1

            total_all = total - day_discount

            print(f'{total_all:.2f}')
        if 22 < day <= 24:
            cakes += count_pastry * 16.98
            print(f'{cakes:.2f}')
