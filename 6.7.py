human1 = {
    'first_name': 'Ivan',
    'last_name': 'ivanov',
    'age': '20',
    'city': 'Khark',
}

human2 = {
    'first_name': 'Petr',
    'last_name': 'petrov',
    'age': '25',
    'city': 'Kyiv',
}

human3 = {
    'first_name': 'vasiliy',
    'last_name': 'vasilevich',
    'age': '70',
    'city': 'dnepr',
}

peoples = [human1, human2, human3]

for people in peoples:
    for key, vault in people.items():
        print(key.title() + ' : ' + vault.title())
    print('\n')
