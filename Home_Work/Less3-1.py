# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = [2, 3, 5, 9, 3]
s = 0
for i in range(1, len(n), 2):
    if i % 2 == 1:
        s += n[i]
print(f"{n} - сумма нечетных элементов равна: {s}")