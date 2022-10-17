# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension

# def find_numbers(numbers: list):
#     new_list = []
#     for x in numbers:
#         if x % 20 == 0 or x % 21 == 0:
#             new_list.append(x)
#     return new_list

list_num = list(range(20, 425))


find_numbers = [x for x in list_num if x % 20 == 0 or x % 21 == 0]
print(find_numbers)