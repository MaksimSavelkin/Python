def take_value():
    while True:
        value = input('Введите число: ')
        try:
            value = float(value)
            return value
        except ValueError:
            print('Это не число. Попробуйте снова...')
            return take_value()