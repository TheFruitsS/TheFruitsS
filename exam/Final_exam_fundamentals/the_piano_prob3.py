def pianist_dict():
    cycle = int(input())
    songsdict = {}
    songli = []

    #songs_dict = {piece: [com, key] for piece, com, key in song}

    for songs in range(cycle):
        song = input().split("|")
        songli.append(song)

    print(songli)
    songs_dict = {piece: [com, key] for piece, com, key in songli}
    print(songs_dict)
    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split("|")
        current_command = command[0]

        if current_command == 'Add':
            pass


pianist_dict()
