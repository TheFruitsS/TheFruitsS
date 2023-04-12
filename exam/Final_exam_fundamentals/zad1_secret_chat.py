message = input()
while True:
    command_main = input()
    if command_main == 'Reveal':
        print(message)
        break
    command = command_main.split(':|:')
    if command_main[0] == 'InsertSpace':
        message[int(command_main[1])] += ' '
        print(message)
