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
        #print(start_end)list


