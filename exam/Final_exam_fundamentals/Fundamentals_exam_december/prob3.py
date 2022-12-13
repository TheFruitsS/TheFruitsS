def special_commands():
    maria_dictionary = {}
    while True:
        command = input()

        if command == 'Complete':
            break

        command = command.split()

        if command[0] == 'Receive':
            quantity = int(command[1])
            food = command[2]
            maria_dictionary[food]['quantity'] += quantity
            food_no_exist_add = command[2]
            if food_no_exist_add not in maria_dictionary[food]:
                maria_dictionary[food] += food_no_exist_add
            if quantity <= 0:
                continue


        if command[0] == 'Sell':
            quantity = int(command[1])
            food = command[2]
            if command[2] not in food:
                print(f"You do not have any {food}.")
            elif maria_dictionary[food]['quantity'] < quantity:
                del maria_dictionary[food]
                print(f"There aren't enough {food}. You sold the last {quantity} of them.")
            else:
                print(f"You sold {quantity} {food}.")

    #print(f'{maria_dictionary[food]}: {maria_dictionary[quantity]}')

special_commands()

# def additional_print_function(maria_dictionary):
#     for food in maria_dictionary:
#         food = maria_dictionary[food]
#         quantity = maria_dictionary[food][1]
#
#         print(f'{food}: {quantity}')
#
#
# def maria_shop():
#
#     shop_dictionary = {}
#
#
#     special_commands(shop_dictionary)
#     additional_print_function(shop_dictionary)



