#1. Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
from decimal import Decimal

P = str(pi)
d = input("Введите число d: ")

print(Decimal(P).quantize(Decimal(str(d))))