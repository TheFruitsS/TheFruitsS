numbers = list(map(int, input().split(', ')))
indexes = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
# lista ima element koito e spisaka sled tova moje da ima for cicle i da varti elementa ot spisaka i sled tova vrashta
#elementa koito sme zadali v na4aloto
print(indexes)
