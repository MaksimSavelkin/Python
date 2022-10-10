# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

import math

def factor(n):
    lis = []
    while n % 2 == 0:
        lis.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            lis.append(i)
            n /= i
    if n > 1:
        lis.append(int(n))
    return lis

num = int(input("Введите число N: "))  
print(*factor(num))  
    