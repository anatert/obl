'''print('-----1-----')
with open('learning_python.txt') as text:
    text = text.read()
    print(text.strip())

print('-----2-----')

with open('learning_python.txt') as text:
    lines = text.readlines()
    for line in lines:
        print(line.strip())'''

print('-----3-----')

with open('learning_python.txt') as text:
    lines = text.readlines()
    text_string = ''
    for line in lines:
        text_string += line.rstrip()

print(text_string.replace('Python', 'C'))






