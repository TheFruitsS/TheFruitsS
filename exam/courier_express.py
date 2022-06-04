kilo = float(input())
favour = input()
distance_km = int(input())
cena = 0
if favour == 'standard':
    if kilo < 1:
        cena = distance_km * 0.03
    elif 1 <= kilo < 10:
        cena = distance_km * 0.05
    elif 10 < kilo <= 40:
        cena = distance_km * 0.10
    elif 40 < kilo <= 90:
        cena = distance_km * 0.15
    elif 90 < kilo <= 150:
        cena = distance_km * 0.20

if favour == 'express':
    if kilo < 1:
        cena = distance_km * 0.03 + kilo * 0.8 * 0.03
    elif 1 <= kilo < 10:
        cena = distance_km * 0.05 + kilo * 0.4 * 0.05
    elif 10 < kilo <= 40:
        cena = distance_km * 0.1 + kilo * 0.05 * 0.10
    elif 40 < kilo <= 90:
        cena = distance_km * 0.15 + distance_km * kilo * 0.02 * 0.15
    elif 90 < kilo <= 150:
        cena = distance_km * 0.2 + kilo * 0.01 * 0.20
print(f"The delivery of your shipment with weight of {kilo:.3f} kg. would cost {cena:.2f} lv.")


