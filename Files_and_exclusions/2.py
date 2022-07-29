'''with open('guest.txt', 'w') as file:
    name = input("What's you name?\n")
    file.write(f'Your name is: {name.title()}')'''

with open('../guests_book.txt', 'a') as file:
    while True:
        name = input('Name:')
        exit = 'q'
        if name == exit:
            break
        elif name != exit:
            print(f'Hello {name.title()}')
            file.write(f'Name: {name.title()}\n')