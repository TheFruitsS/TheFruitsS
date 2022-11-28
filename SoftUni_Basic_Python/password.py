username = input()
password = input()

while True:
    data = input()
    if data == password:
        print(f'Welcome {username}!')
        break
#dokato ne savpadnat dvete imena nqma da prikliuchi za password
# primer username and David David -->Welcome David