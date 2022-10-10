# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import numpy

def non_set(set):
    tu_s = []
    for i in set:
        if set.count(i) > 1:
            continue
        else:
            tu_s.append(i)
    return tu_s

items = numpy.random.randit(10, size = 10)
items_set = list(items[ : 10])
print(*items_set)
print(*non_set(items_set))