responses = {

}
polling = True
while polling:
    name = input('\nName: ')
    local = input('\nLocal: ')
    responses[name] = local
    repeat = input('Continue (y/n)?')
    if repeat == 'n':
        polling = False
    elif repeat == 'y':
        polling = True
print('\n______Results_______')
for name, response in responses.items():
        print(f'\nName: {name.title()} \nLocal: {local.title()}')
