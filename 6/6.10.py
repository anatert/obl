names = {'Marina': ["1", "2"], 'Serg': ["3", "4"], 'Lena': ["5", "6"], 'Tol': ["7", "8"]}
for name, numbers in names.items():
    print("\n" + name + ' favorite numbers are:')
    for number in numbers:
        print('\t' + number)