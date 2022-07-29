with open('pm.txt', 'r') as pm:
    lines = pm.readlines()
    p_string = ''
    for line in lines:
        p_string += line.strip()
    date = input('Date "ddmmyy":\n')
    if date in p_string:
        print('Дата есть в числе пи')
    else:
        print('Даты нет в числе пи')

