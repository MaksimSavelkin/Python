def init_complex():
    while True:
        a = (input("Введите действительную часть числа: "))
        b = (input("Введите мнимую часть числа: "))
        if not a.isdigit() or b.isdigit():
            print('Ошибка. Повторите ввод')
            continue
        a, b = int(aa), int(b)
        break
    return complex (a, b)