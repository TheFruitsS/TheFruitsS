import re
data = ''

while True:
    command = input().split(' ')


    if command[0] == 'End':
        break

    if command[0] == 'Print':
        print(data)

    if command[0] == 'Add':
        data = data + command[1]

    if command[0] == 'Upgrade':
        find_chr = command[1]
        replace_chr_num = ord(str(find_chr))+1
        replace_chr = chr(replace_chr_num)
        data = data.replace(str(find_chr), replace_chr)

    if command[0] == 'Index':
        str_index = data.index(command[1])
        if not str_index:
            print('None')

if command[0] == 'Remove':
    substring = command[1]
    data = re.split(data,substring)