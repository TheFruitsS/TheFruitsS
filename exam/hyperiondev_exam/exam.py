# Christmas_budget = 0
# # salary = 1250
# # rent = 650
# # util = 175
# # deductions = salary - rent - util
# # saving = deductions * 25 / 100
# # saving_shoping_Dec = 3 * saving
# # print(f'You must save {saving:.2f} each month to meet this target?')
# # print(f'The amount you will have in December for Christmas shopping is {saving_shoping_Dec:.2f} ')
# #
# # #Weight is measured in kilograms and height is measured in metres.
# # weight = float(input())
# # height = float(input())
# # BMI = weight / height ** 2
# # print(f'Your BMI:{BMI: .2f}')
# #
# # user = input(f'Please, enter a 6-letter word:')
# # if len(user) == 6:
# #     print(user[::-1])
# # else:
# #     print(f'Please, try again enter a 6-letter word')
# # sentence = 'I!am!a!coding!genius!'
# # print(sentence.replace('!', ' ')[::-1])
#
# # user = input()
# # if int(user) % 2 == 0:
# #   print ("fizz")
# # else:
# #   print ("buzz")
# # animals = ['lion', 'zebra', 'donkey', 'giraffe']
# # animals.pop(1)
# # animals.append('cheetah')
# # animals.pop(-1)
# # print(animals)
# # username = input()
# # user_email = input()
# # print(f'Hi {username}! We will be contacting you shortly at {user_email}')
# #
#
# # count = 0
# # while int(input()) > 0:
# #
# #       count += 1
# #
# # print(count)
# #
# # hour = int(input())
# # guard = True
# # if hour in range(7, 18):
# #     print('You\'re in the Campus is open')
# # elif hour in range(0,7) or hour in range(17, 24):
# #     if guard == False:
# #         print('Guard is not there')
# #     if guard == True:
# #         print('You\'re in!')
# # else:
# #    print('Please enter valid hour.')
#
# # For this task you are required to use your knowledge of lists from the Coding Preparation section to manage a number
# # of items in an ordered structure.
# #
# # You are going to be creating a program that represents the movements of the line for the lady's bathroom.
# # To begin, create a list that represents the line, it must contain the five names of the women initially waiting (you can make these up).
# #
# # The following events occur, and you must represent them in the list and print the list out after each action.
# #
# # A woman named Jenny arrives who only wanted to check her lipstick, she asks to join the front of the line,
# # and all the women let her.
# # The woman third in line’s phone started ringing, and she left the line to answer.
# # A new woman named Alice joined the line.
# # Use the trinket IDE below to write and test your code.
# #'Alice'
# # woman_toilet = ['Sara','Amy', 'Eva', 'Jenny']
# # print(woman_toilet)
# # woman_toilet.pop(-1)
# # woman_toilet.insert(0, 'Jenny')
# # print(woman_toilet)
# # woman_toilet.pop(2)
# # print(woman_toilet)
# # woman_toilet.append('Alice')
# # print(woman_toilet)
#
# # Create a variable to store the given string "You can have data without information,
# # but you cannot have information without data."
# # Convert the given string to lowercase
# # Create a list containing every lowercase letter of the English alphabet
# #
# # for every letter in the alphabet list:
# #     Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
# #     for every letter in the given string:
# #         if the letter in the string is the same as the letter in the alphabet list
# #             increase the value of the frequency variable by one.
# #     if the value of the frequency variable does not equal zero:
# #         print the letter in the alphabet list followed by a colon and the value of the frequency variable
# # store_string = input()
# # store_string.lower()
# # store_list = [i for i in store_string]
# #
# # alphabet_lower = [chr(i) for i in range(97, 123)]
# #
# #
# # for matches in alphabet_lower:
# #     counter = store_list.count(matches)
# #     print(f'{matches}:{counter}')
# # size = int(input())
# # for row in range(0, size):
# #     for col in range(0, size):
# #
# #         # Here end is used to stay in same line
# #         if (row == col):
# #             print("1 ", end="   ")
# #         else:
# #             print("1 ", end=" ")
# #     print()
#
# cells = [1, 1, 0, 0, 0, 1, 0]
# print(cells)
# print(f"You free the prisoner in the :{cells.index(1) + 1} cell")
# print(f'The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked')
#
# rever = []
#
# def invert(cellli, reverli):
#     for cell in cellli:
#         if str(cell) == '1':
#
#             lockedcell = str(cell).replace(str(cell), '0')
#             reverli.append(lockedcell)
#
#         if str(cell) == '0':
#             unlockedcell = str(cell).replace(str(cell), '1')
#             reverli.append(unlockedcell)
#
#     print(rever)
#
#
#
# def switch(firs, sec):
#     firs.clear()
#     firs.extend(sec)
#     sec.clear()
#
#
# for counter in range(0, cells.count(1)):
#
#     invert(cells, rever)
#
#     switch(cells, rever)