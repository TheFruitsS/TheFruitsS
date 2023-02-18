row1 = int(input())
row2 = int(input())
row3 = int(input())
row4 = int(input())
row5 = int(input())
mass1 = row1 * row4 / 900
mass2 = row2 * row4 / 400
mass3 = row3 * row4 / 400
summass = mass1 + mass2 + mass3
cal1g = row4 / summass
finca  = 100 - row5
cal = finca * cal1g / 100
print(f'{cal:.4f}')