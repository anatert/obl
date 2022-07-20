dictionary_1 = {
    'country': 'country_1', 'population': 'population_1', 'fact': 'fact_1',
}
dictionary_2 = {
    'country': 'country_2', 'population': 'population_2', 'fact': 'fact_2',
}
dictionary_3 = {
    'country': 'country_3', 'population': 'population_3', 'fact': 'fact_3',
}

dictionarys = [
    dictionary_1, dictionary_2, dictionary_3
]

for city in dictionarys:
    for k,v in city.items():
        print(k.title() + ' : ' + v.title())
    print('\n')


