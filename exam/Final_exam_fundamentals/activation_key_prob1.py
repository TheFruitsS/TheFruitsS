#input -letters and numbers only
#receiving strings until command 'Generate' break
# commands
# "Contains>>>{substring}" ,
# "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}"
#Slice>>>{startIndex}>>>{endIndex}"
import re
activation_key = input()
while True:
    command = input()

    pattern_slice = r"Slice"
    slice_command = re.match(pattern_slice, command)

    pattern_Upper = r"Upper"
    flip_command_upper = re.search(pattern_Upper, command)

    pattern_lower = r"Lower"
    flip_command_lower = re.search(pattern_lower, command)

    pattern_contains = r"Contains"
    contains_command = re.match(pattern_contains, command)

    if command == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break

    if slice_command:

        pattern_num_for_slice = r"\d+"
        start_end = re.findall(pattern_num_for_slice, command)
        start_end = list(map(int, start_end))

        first_slice = activation_key[:start_end[0]]
        second_slice = activation_key[start_end[1]:]
        activation_key = first_slice + second_slice
        print(activation_key)

    if flip_command_upper:

        pattern_num_for_flip = r"\d+"
        start_end = re.findall(pattern_num_for_flip, command)
        start_end = list(map(int, start_end))
        first_slice = activation_key[:start_end[0]]
        second_slice = activation_key[start_end[1]:]
        middle = slice(start_end[0], start_end[1])
        upper_text = activation_key[middle].upper()
        activation_key = first_slice + upper_text + second_slice
        print(activation_key)

    if flip_command_lower:
        pattern_num_for_flip = r"\d+"
        start_end = re.findall(pattern_num_for_flip, command)
        start_end = list(map(int, start_end))
        first_slice = activation_key[:start_end[0]]
        second_slice = activation_key[start_end[1]:]
        middle = slice(start_end[0], start_end[1])
        upper_text = activation_key[middle].lower()
        activation_key = first_slice + upper_text + second_slice
        print(activation_key)

    if contains_command:
        substring_pattern = command[11:]
        contains_command = re.search(substring_pattern, activation_key).group()
        if contains_command in activation_key:
            print(f'{activation_key} contains {substring_pattern}.')
        else:
            print('Substring not found!')