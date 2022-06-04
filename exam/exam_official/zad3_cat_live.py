# ходът се чете от конзолата и съдържа точно 2 реда:
#    • Порода на котката  –  текст  –  една от възможностите: "British Shorthair",
#    "Siamese", "Persian", "Ragdoll", "American Shorthair" или "Siberian"
#   • Пол на котката  – символ –  'm' или 'f'
from math import floor

cat_type = input()
cat_gender = input()

if cat_gender == 'm':
    if cat_type == 'British Shorthair':
        age = 13
    elif cat_type == 'Siamese':
        age = 15
    elif cat_type == 'Persian':
        age = 14
    elif cat_type == 'Ragdoll':
        age = 16
    elif cat_type == 'American Shorthair':
        age = 12
    elif cat_type == 'Siberian':
        age = 11

elif cat_gender == 'f':
    if cat_type == 'British Shorthair' :
        age = 14
    elif cat_type == 'Siamese':
        age = 16
    elif cat_type == 'Persian':
        age = 15
    elif cat_type == 'Ragdoll':
        age = 17
    elif cat_type == 'American Shorthair':
        age = 13
    elif cat_type == 'Siberian':
        age = 12
else:
    print(f'{cat_type} is invalid cat!')

age_per_months = age * 12
cat_months = age_per_months / 6
cat_months = floor(cat_months)

print(f'{cat_months} cat months')



