encrypted_message = input()

while True:
    command = input().split('|')
    current_command = command[0]

    if current_command == 'Decode':
        print(f"The decrypted message is: {encrypted_message}")
        break

    elif current_command == 'Move':
        moving_letters = int(command[1])
        encrypted_message = encrypted_message[moving_letters:] + encrypted_message[:moving_letters]

    elif current_command == 'Insert':
        given_letter = command[2]
        index_letter = int(command[1])
        encrypted_message = encrypted_message[:index_letter] + given_letter + encrypted_message[index_letter:]

    elif current_command == 'ChangeAll':
        encrypted_message = encrypted_message.replace(command[1], command[2])
