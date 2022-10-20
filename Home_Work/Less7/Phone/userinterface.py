# user interface - приветствие, импортировать данные из текстового файла, 

# ввести вручную(фамилия имя телефон описание), показать существующие данные

import show
import logg
import error
import convert
import write
print('Добрый день!\n')


def start():
    while True:
        print("ГЛАВНОЕ МЕНЮ")
        print("1. Показать телефонный справочник")
        print("2. Ввести новые данные в справочник")
        print("3. Импортировать данные из файла txt")
        print("0. Выход\n")
        logg.start_app()
        token = error.make_choise(0, 3)

        1 == == 1:
            logg.next_step()
            show.show_data()
            logg.show_data()
            
        2 == == 2:
            logg.next_step()
            a = error.error_name('фамилию')
            write.init_surname(a)
            b = error.error_name('имя')
            write.init_name(b)
            c = error.error_phone('номер телефона')
            write.init_phone(c)
            write.init_enough((input("Введите дополнительные данные: ")))
            write.write_from()
            logg.fill()
        
        if token == 3:
            logg.next_step()
            d = error.file_name()
            error.file_exist(d)

        if token == 0:
            print('До скорых встреч!')
            quit()


start()