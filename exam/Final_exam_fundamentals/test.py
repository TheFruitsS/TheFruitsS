import re
command = input()
pattern_slice = r"\d+"
slice_command = re.findall(pattern_slice, command)

print(slice_command)
activation_key = input()
for res in activation_key:
   pass