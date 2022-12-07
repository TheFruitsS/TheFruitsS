multiplevalues_dict = {'Lamborghini Veneno': [11111, 74], 'Bugatti Veyron': [12345, 67], 'Koenigsegg CCXR': [67890, 12], 'Aston Martin Valkryie': [99900, 50]}

for car in multiplevalues_dict:
    print(f'Model{car}')
    print(f'Mileage:{multiplevalues_dict[car][0]}')
    print(f'Fuel Consumption:{multiplevalues_dict[car][1]}\n')