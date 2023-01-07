def list_of_lists(txtli):
    list1 = []
    lenght = 0
    for x in txtli:
        list1.extend(x)
        for y in x:

            lenght += len(y)
    result = ', '.join(list1)
    print(f"Destinations: {result}")
    print(f"Travel Points: {lenght}")

def destination_map():
    import re
    data = input()
    pattern = r'\=[A-Z][a-z]{2,}\=|\=[A-Z][a-z]{2,}\s[A-Za-z]+\=|\/[A-Z][a-z]{2,}\/|\/[A-Z][a-z]{2,}\s[A-Za-z]+\/'
    matches = re.findall(pattern, data)

    if matches:

        txtli = [((x.replace('=', ',').replace('/', ','))[1:-1]).split(',')
                 for x in matches]

        list_of_lists(txtli)
    else:
        print(f"Destinations:")
        print(f'Travel Points: 0')


destination_map()