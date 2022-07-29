with open('book.txt', 'r') as book:
    lines = book.read()
    print(lines.lower().count('the'))




