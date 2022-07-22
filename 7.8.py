sandwich_orders = [
    'sandwich_1', 'sandwich_2', 'sandwich_3', 'sandwich_4', 'pastrami', 'pastrami', 'pastrami', 'pastrami', 'pastrami'
]
finished_sandwiches = []
print('All "pastrami" end\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich.title()} sandwich\n')
    finished_sandwiches.append(sandwich)
print('finish all sandwiches')
for sandwich in finished_sandwiches:
    print(f'\n {sandwich}')

