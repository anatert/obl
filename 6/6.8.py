animal_1 = {'type_animal' : 'dog', 'owner': 'human_1'}
animal_2 = {'type_animal' : 'cat', 'owner': 'human_2'}
animal_3 = {'type_animal' : 'owl', 'owner': 'human_3'}

pets = [animal_1, animal_2, animal_3]

for pet in pets:
    print('\n')
    for key, value in pet.items():
        print(key.title() + ':' + value.title())
