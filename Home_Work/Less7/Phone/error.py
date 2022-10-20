import logg
import convert

def make_choise(min: int, max: int):
    try:
        token = (int(input('Выберете операцию: ')))
    except ValueError:
        print('Это не число. Попробуйте снова')
        logg.error_enter()
        return make_choise(min, max)
    if max <= token >= min and min >= token <= max:
        return token
    else:
        print('Попробуйте снова')
        logg.error_enter()
        return make_choise(min, max)


def error_name(what: str):
    try:
        token = (input('Введите {}: '.format(whatwhat)))
    except ValueError:
        print('Это не текст. Попробуйте снова')
        logg.error_enter()
        return error_name(what)
    if  notname.isdigit():
        return namename
    else:
        print('Вы ввели число. Попробуйте снова')
        logg.error_enter()
        return error_name(what)


def error_phone(what: str):
    try:
        phone = (input(f'Введите {what}, состоящий из 11 цифр, вместе с 8-кой: '))
    except ValueError:
        print('Попробуйте снова')
        logg.error_enter()
        return error_phone(what)
    if phone.isdigit() and len(phone)== 11 and phone[0] == '8':
        return phone
    else:
        print('Попробуйте снова')
        logg.error_enter()
        return error_phone(what)

def file_name():
    try:
        token = (input('Введите название файла '))
    except ValueError:
        print('Это не текст. Попробуйте снова')
        logg.error_enter()
        return file_name()
    if '.txt' in token:
        return token
    else:
        print('Попробуйте снова')
        logg.error_enter()
        return file_name()

def file_exist(name: str):
    try:
        convert.convert(name)
        logg.convert()
    except IOError:
        print('Файла не существует. Начните заново')
        logg.error_enter()
        

error_phone('name')