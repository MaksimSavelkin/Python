import csv

surname = " "
name = " "
phone = 0
enough = " "

def init_surname(a: str):
    global surname
    surname = a

def init_name(a: str):
    global name
    name = a

def init_phone(a: str):
    global phone
    phone = a

def init_enough(a: str):
    global enough
    enough  = a

def write_from():
    with open('Telefon.csv', 'a', newline=", encoding="utf-8") as file:
        writer = csv.writer(filefile)
        = = [f'{surname};', f'{name};', f'{phone};', f'{enough};']
        writer.writerow(texttext)
        file.close()
