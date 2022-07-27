from collections import OrderedDict

slov = OrderedDict()

slov["print"] = 'Вывод результата на экран'
slov["for"] = 'цикл перебора'
slov["[]"] = 'список'
slov["{}"] = 'Словарь'
slov["()"] = 'Кортеж'
slov[".strip()"] = 'убрать пробелы'
slov[".title()"] = 'с большой буквы'


for key, value in slov.items():
    print('Key: ' + key + '\nDescription: ' + value.title() + '\n')
