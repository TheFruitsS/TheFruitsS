the_most_powerful_word_counter = 0
the_most_powerful_word = ''

while True:
    word = input()

    if word == 'End of words':
        break

    current_counter = 0

    for ch in word:
        current_counter += ord(ch)

    if word[0].lower() in 'aeiouy':
        current_counter *= len(word)
    else:
        current_counter = int(current_counter / len(word))

    if current_counter > the_most_powerful_word_counter:
        the_most_powerful_word_counter =
