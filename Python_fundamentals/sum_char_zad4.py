
n_numbers_in_line = int(input())
ascii_sum = 0


for n_numbers_in_line in range(n_numbers_in_line):
    a_letter_per_line = input()
    ascii_sum += ord(a_letter_per_line)

print(f'The sum equals: {ascii_sum}')












