#3.Задайте список из n чисел
# последовательности (1+1/n)^n и выведите
# на экран их сумму.
#*Пример:*
#- Для n = 6: {1: 2, 2: 2.25, 3: 2.37,
#4: 2.44, 5: 2.49, 6: 2.52}

n = int(input('Введите число N: '))
D = dict()
j = 1
for i in range(n):
  D[j] = 1 + 1 / j
  j += 1
print(D)