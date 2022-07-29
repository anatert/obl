while True:
    try:
        x = (input('введите первое число: '))
        y = (input('введите второе число: '))
        print(int(x) + int(y))
    except ValueError:
        print("Введите чило а не букву")