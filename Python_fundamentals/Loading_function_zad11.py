def loading_function(number):
    if number == 100:
       return '100% Complete!\n[%%%%%%%%%%]'
    if number < 100:
        percentage = int(number / 10)
        my_list = (["."".""."".""."".""."".""."".".replace(".", "%", percentage)])

        x = "".join(my_list)


        return f'{number}% [{x}] ' \
          f'\nStill loading...'


loading_input = int(input())
print(loading_function(loading_input))
