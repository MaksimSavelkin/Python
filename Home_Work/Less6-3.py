# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

from itertools import groupby



def dict_name(count: int):
    list_names = []
    dict_of_names = {}
    for i in range(count):
        list_names.append(input('Введите имя сотрудника: '))
    for name in sorted(list_names):
        first_letter = name[0]
        if first_letter not in dict_of_names:
            dict_of_names[first_letter] = [name]
        else:
            dict_of_names[first_letter].append(name)
    return dict_of_names

print(dict_name(3))

from itertools import groupby

def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина"))