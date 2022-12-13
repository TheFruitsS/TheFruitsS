import re
data = int(input())


for _ in range(data):
    str_in = input()
    str_pattern = r'U\$([A-Za-z]{3,})U\$P\@\$([A-Za-z]{5,}\d{1,})P\@\$'
    #{3,}in this pattern regex find 3 or more matches if was only{3} that will match exactly 3 matches not less not more
    str_valid = re.search(str_pattern, str_in)

    if str_valid:
        username, password = str_valid.groups()
        #count_matches = username.count(username)

        print(f'Registration was successful Username: {username}, Password: {password}')
        #exit(print(f"Successful registrations: {count_matches}"))

    else:
        print(f"Invalid username or password")

    for count_matches in str_valid:
        count_matches
