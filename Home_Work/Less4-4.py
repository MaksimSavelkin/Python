# 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать
#  в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def creates(k, m, n):
    return[randint(m, n) for i in range(k + 1)]

def polyn(input_list):
    polinomial = []
    for i in range(len(input_list)):
        if input_list[-1 - i] !=0:
            polinomial.insert(0, str(input_list[-1 - i]) + "*x^" + str(i))
    polinomial_str = " + ".join(polinomial)
    polinomial_str += "= 0"
    polinomial_str = polinomial_str.replace(" 1*", " ")
    polinomial_str = polinomial_str.replace("^1", " ")
    polinomial_str = polinomial_str.replace("x^0", "1")
    polinomial_str = polinomial_str.replace("*1", " ")
    if polinomial_str[0] == "1" and polinomial_str[1] == "*":
        n = 2
        polinomial_str = polinomial_str[n:]
    return polinomial_str

k = int(input("Введите стпень уравнения: "))
m = int(input("Введите нижнюю границу чисел: "))
n = int(input("Введите верхнюю границу чисел: "))
input_list = creates(k, m, n)
polinomial = polyn(input_list)

print(input_list)

with open('C:\Users\Максим\Desktop\GB\gb\Python\Home_Work\Home Work 4-4.txt', 'a') as data:
    data.write(f"\n{polyn(input_list)}")
