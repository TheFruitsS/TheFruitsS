def lenght_password(some_input):
    if 6 <= len(some_input) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False
def only_letters_and_digits(some_input):
    if some_input.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False

def check_numbers_count(some_input):
    digit_counter = 0
    for character in some_input:
        if character.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False

password_input = input()
password_input_list = [lenght_password(password_input), \
                       only_letters_and_digits(password_input), \
                        check_numbers_count(password_input)]

if all(password_input_list):
    print("Password is valid")

