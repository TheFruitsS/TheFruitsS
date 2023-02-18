row0 = float(input())
row1 = int(input())
row2 = int(input())
row3 = int(input())
row4 = int(input())
row5 = int(input())
price1 = row1 * 0.60
price2 = row2 * 7.20
price3 = row3 * 3.60
price4 = row4 * 18.20
price5 = row5 * 22
summa = price1 + price2 + price3 + price4 + price5
arts = row1 + row2 + row3 + row4 + row5
discount = 0
if arts > 25:
    discount = 35 * summa / 100

finpr  = summa - discount

host = finpr * 10 / 100

finalpr = finpr - host
finalleft = finalpr - row0
noten = row0 - finalpr
if finalpr > row0:
    print(f'Yes! {finalleft:.2f} lv left.')
else:
    print(f'Not enough money! {noten:.2f} lv needed.')