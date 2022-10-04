# 4.Реализуйте алгоритм перемешивания списка

import random

def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print(mixed_list)