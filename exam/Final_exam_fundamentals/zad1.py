message = input()

while True:
    command = input().split(' ')
    current_command = command[0]

    if command[0] == 'For' and command[1] == 'Azeroth':

        break

    elif current_command == 'GladiatorStance':
        message = message.upper()
        print(message)

    elif current_command == 'DefensiveStance':
        message = message.lower()
        print(message)

    elif current_command == 'Dispel':
        message = message[:int(command[1])]  + command[2] + message[int(command[1]) + 1:]
        if message:
            print('Success!')
        else:
            print("Dispel too weak.")
    elif command[0] == 'Target' and command[1] == 'Change':
        message = message.replace(command[2], command[3])
        if message:
            print(message)
        else:
            print(message)
    elif command[0] == 'Target' and command[1] == 'Remove':
        message = message.replace(command[2], '')
        if message:
            print(message)
        else:
            continue
    else:
        print("Command doesn't exist!")

