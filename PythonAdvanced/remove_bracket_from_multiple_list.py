my_list = [['bobby'], ['hadz'], ['.', 'com']]

flat_list = [x for xs in my_list for x in xs]

print(flat_list)  # 👉️ ['bobby', 'hadz', '.', 'com']

flat_list_no = " ".join(map(str, flat_list))
print(flat_list_no)

