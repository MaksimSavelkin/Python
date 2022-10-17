# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import choices
# def sorted_list(numbers: list):
#     new_list = []
#     for x in range(1, len(numbers)):
#         if numbers[x] > numbers[x-1]:
#             new_list.append(numbers[x])
#     return new_list

list_num = choices(range(1, 20), k=9)
print(list_num)

sorted_list = [list_num[x] for x in range(1, len(list_num)) if list_num[x] > list_num[x-1]]
print(sorted_list)