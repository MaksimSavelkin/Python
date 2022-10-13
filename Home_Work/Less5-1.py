# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def str_ed(my_str, sym):
    return(" ".join([word for word in my_str.split() if sym not in word]))

input_str = input("Введите текса: \n")
text_1 = input("Введиите символы для удаления: ")
print(str_ed(input_str, text_1))