# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = False
y = False
z = False

if not(x or y or z) == (not x) and (not y) and (not z):
    print(True)
else:
    print(False)