# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

file1 = "C:\Users\Максим\Desktop\GB\gb\Python\Home_Work\Home_Work_4-5_1.txt"
fiel2 = "C:\Users\Максим\Desktop\GB\gb\Python\Home_Work\Home_Work_4-5_2.txt"
file_sum = "C:\Users\Максим\Desktop\GB\gb\Python\Home_Work\Home_Work_4-5_sum.txt"

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def polinomial_list(pol):
    pol = pol.replace("=0", "")
    pol = pol.replace("+ ", "")
    pol_list = pol.split()
    return pol_list

pol_sun_str = " + ".join(polinomial_list(read_pol(file1)) + polinomial_list(read_pol(file2)))
pol_sun_str += " = 0 "
with open(file_sum, 'a') as data:
    data.write(pol_sun_str + "\n")