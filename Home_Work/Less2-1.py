# 1. Напишите программу, которая принимает на
# вход вещественное число и показывает сумму
# его цифр.
#*Пример:*
#- 6782 -> 23
#- 0,56 -> 11
a = input('Введите число:')
s = 0
count = 10 ** (len(a) - 2)
a = int(float(a) * count)
while a > 0:
  s += a % 10
  a //= 10
print(s)