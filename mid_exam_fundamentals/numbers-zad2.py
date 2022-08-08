my_list = input().split()

while True:
    command = input().split()

    if "Finish" in command:
        break

    if 'Add' in command and int(1):
        my_list.append(command.pop(1))
    if "Remove" in command and int(1):
        my_list.remove(command.pop(1))
    if "Replace" in command and int(1) and int(2):
        value = command.pop(1)
        replacement = command.pop(1)

        i = my_list.index(value)
        my_list = my_list[:i] + [f'{replacement}'] + my_list[i + 1:]
    if "Collapse" in command and int(1):
        value_of_collapse = command.pop(1)
        list_collapse = ([int(element) for element in my_list if int(element) // int(value_of_collapse) > 0])
        my_list.clear()
        for i in list_collapse:
            my_list.append(str(i))

new_list = ' '.join(my_list)
print(new_list)