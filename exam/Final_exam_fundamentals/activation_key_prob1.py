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
    slice_command = (re.match(pattern_slice, command)).group()
    if command == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break

    if slice_command:

        pattern_num_for_slice = r"\d+"
        start_end = re.findall(pattern_num_for_slice, command)
        start_end = list(map(int, start_end))
        print(start_end)
        first_slice = activation_key[:start_end[0]]
        second_slice = activation_key[start_end[1]:]
        activation_key = first_slice + second_slice
        print(activation_key)

