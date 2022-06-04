budget = float(input()) # izvan while zashtoto e postoqnna velichina
costs = 0 # variaciq koqto ne se otpechatva izkarana e van
counter_of_products = 0 # broq4 na produkti sashto e izkaran van
budget_condition = False # budget condition e izkarano van
needed_money = 0  # neobhodimite pari za izkarani van
# vsichki variable sa izkarani van osven tazi koqto ne se varti i sa im dadeni stoinosti 0
while True:
    name_of_product = input() # imeto na produkta moje da e razlichno i go vartim zatova e v while

    if name_of_product == 'stop': # ako zadadem za ime na produkt stop shte sprem cikala
        break

    product_price = float(input()) # cenata na produkta e cqlo chislo i e v while zashtoto se smenq dokato dostigne budget
    counter_of_products += 1 # broq4 na produkti ne iskame da se pokazva v konzlolata i zatova ne mu davame input
    # raven e na broq4 na produkti = broq4 na produkti + 1

    if counter_of_products % 3 == 0: # proverka ako broq4a na produkti se pobira 3
        product_price /= 2          # togava cenata na produkta koqto se pokazva da e ravna na polovina

    if product_price > budget:         # ako cenata na produkta e po golqma ot budget
        budget_condition = True        # togava uslovieto za budgeta e vqrno  imame izkarano predi tova izvan cikala che uslovieto za budget ne e vqrno
        needed_money = product_price - budget # togava neobhodimite pari = cenata na produkta - budget
        counter_of_products -= 1    # broq4 na produkti e = broq na produktite -1
        break

    costs += product_price  # razhodite = razhodite + cenata na produkta
    budget -= product_price  # budget = budget + cenata na produkta

if not budget_condition: # ako ne e izpalneno budget uslovieto
    print(f'You bought {counter_of_products} products for {costs:.2f} leva. ') # pokaji mi broq na produktite za razhodi costs

else:
    print(f'You don`t have enough money!\nYou need {needed_money:.2f} leva!')   # ako ne nqmash dostatachno pari  imash nujda ot edi kolko si pari
