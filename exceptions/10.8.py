filenames = ['cats.txt', 'dogs.txt']
try:
    for file in filenames:
        with open(file) as text:
            text = text.read()
        print(text)
        print('\n')
except FileNotFoundError:
    pass