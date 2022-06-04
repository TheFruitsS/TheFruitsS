country = input()
device = input()
difficulty = 0
evaluation = 0

if country == 'Bulgaria':
    if device == 'ribbon':
        difficulty = 9.6
        evaluation = 9.4
    elif device == 'hoop':
        difficulty = 9.55
        evaluation = 9.75
    elif device == 'rope':
        difficulty = 9.5
        evaluation = 9.4

elif country == 'Russia':
    if device == 'ribbon':
        difficulty = 9.1
        evaluation = 9.4
    elif device == 'hoop':
        difficulty = 9.3
        evaluation = 9.8
    elif device == 'rope':
        difficulty = 9.6
        evaluation = 9

elif country == 'Italy':
    if device == 'ribbon':
        difficulty = 9.2
        evaluation = 9.5
    elif device == 'hoop':
        difficulty = 9.45
        evaluation = 9.35
    elif device == 'rope':
        difficulty = 9.7
        evaluation = 9.15

total_score = difficulty + evaluation
diff = 20 - total_score
needed_percent = (diff / 100)
print(f'The team of {country} get {total_score:.3f} on {device}')
print(f'{needed_percent:.2f}%')








