kilo = float(input())
if 0.01 <= kilo <= 150:
   pass
else:
    exit('Not valid')

favour = input()
if favour == 'standard' or favour == 'express':
    pass
else:
    exit('Not valid')
distance_km = int(input())
if 0 < distance_km <= 1000:
    pass
else:
    exit('Not valid')


cenast = 0
cenaexp = 0


if favour == 'standard':
    if distance_km <= 1000 or distance_km > 0 and kilo > 0.01 or kilo <= 150.00:

        if kilo < 1:
            cenast = distance_km * 0.03
        elif 1 <= kilo < 10:
            cenast = distance_km * 0.05
        elif 10 < kilo <= 40:
            cenast = distance_km * 0.10
        elif 40 < kilo <= 90:
            cenast = distance_km * 0.15
        elif 90 < kilo <= 150:
            cenast = distance_km * 0.20
        print(f'The delivery of your shipment with weight of {kilo:.3f} kg. would cost {cenast:.2f} lv.')
if favour == 'express':
    if distance_km <= 1000 or distance_km > 0 and kilo > 0.01 or kilo <= 150.00:
        if kilo < 1:
            cenaexp = distance_km * 0.03 + kilo * 0.8 * 0.03
        elif 1 <= kilo < 10:
            cenaexp = distance_km * 0.05 + kilo * 0.4 * 0.05
        elif 10 < kilo <= 40:
            cenaexp = distance_km * 0.1 + kilo * 0.05 * 0.10
        elif 40 < kilo <= 90:
            cenaexp = distance_km * 0.15 + distance_km * kilo * 0.02 * 0.15
        elif 90 < kilo <= 150:
            cenaexp = distance_km * 0.2 + kilo * 0.01 * 0.20
        print(f'The delivery of your shipment with weight of {kilo:.3f} kg. would cost {cenaexp:.2f} lv.')

