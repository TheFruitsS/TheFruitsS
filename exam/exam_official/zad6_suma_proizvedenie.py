# Да се напише програма, която проверява сумата и произведението на всички числа, които са комбинация от четирите цифри a, b, c и d.
# В проверката участва и още едно число - n, което се чете от конзолата.
# За всяка комбинация четирите цифри a, b, c и d се променят по следния начин:
#   • a се мени от 1 до 9
#  • b се мени от 9 до а
# • c се мени от 0 до 9
# • d се мени от 9 до c
# Ако сумата (a + b + c + d) е равна на произведението (a * b * c * d) и едновременно с това n завършва на 5, трябва да се принтира числото abcd.
# Ако разделим произведението (a * b * c * d) на сумата (a + b + c + d) и получим 3 (целочислено), и едновременно с това n се дели на 3 без остатък, трябва да се принтира числото dcba.
# Програмата трябва да принтира на конзолата само първата валидна комбинация.
# Ако не се намери такова число abcd или dcba, трябва да се принтира "Nothing found".
# Вход:
# От конзолата се прочита 1 ред:
#  • n - цяло число в интервала [100…1000]
# Изход:
# На конзолата се отпечатва 1 ред:
#   • Ако се намери валидна комбинация:
#      ◦ "{number}", където {number} е комбинацията abcd или комбинацията dcba
# • Ако НЕ се намери такава комбинация:
#    ◦ "Nothing found"

number = input()
a = int()
b = int()
c = int()
d = int()
condition = False

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):

                if (a + b + c + d) == (a * b * c * d) and int(number[len(number) - 1]) == 5:
                    print(a, b, c, d)
                    condition = True
                    #break nqma nujda ot tova break tai kato proverqva za condition i vsi4ko minava prez tazi proverka
                    # ako ne slojim condition a samo break kato vlezne proveri shte prodalji i shte otpe4ata vsi4ki
                    # kombinacii
                if (a * b * c * d) // (a + b + c + d) == 3 and int(number) % 3 == 0:
                    print(d, c, b, a)
                    condition = True
                    #break
                if condition:
                    break
        if condition:
            break
    if condition:
        break
else:
    print(f'Nothing Found')


