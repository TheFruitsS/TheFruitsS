def pianist_dict():
    cycle = int(input())
    songli = []

    for songs in range(cycle):
        song = input().split("|")
        songli.append(song)

    songs_dict = {piece: [com, key] for piece, com, key in songli}

    while True:
        command = input()

        if command == 'Stop':
            break
        command = command.split("|")
        current_command = command[0]

        if current_command == 'Add':
            if command[1] in songs_dict.keys():
                print(f"{command[1]} is already in the collection!")
            else:
                songs_dict[command[1]] = [command[2], command[3]]
                print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        if current_command == 'Remove':
            if command[1] in songs_dict.keys():
                songs_dict.pop(command[1])
                print(f"Successfully removed {command[1]}!")
            else:
                print(f"Invalid operation! {command[1]} does not exist in the collection.")
        if current_command == 'ChangeKey':
            if command[1] in songs_dict.keys():
                songs_dict[command[1]][1] = command[2]
                print(f"Changed the key of {command[1]} to {command[2]}!")
            else:
                print(f"Invalid operation! {command[1]} does not exist in the collection.")

    for piece ,[com, key] in songs_dict.items():
        print(f"{piece} -> Composer: {com}, Key: {key}")
    return songs_dict

pianist_dict()