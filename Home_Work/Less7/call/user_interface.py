from re import T
import model_div
import model_sum
import model_pow
import model_sub
import model_mult
import model_sqrt
import comply
import main
import logg

print('Добро пожаловать в Калькулятор!\n')


def start():
    while True:
        print("ГЛАВНОЕ МЕНЮ")
        print("1. Работа с рациональными числами")
        print("2. Работа с комплексными числами")
        print("0. Выход\n")
        logg.start_app()
        try:
            token = int(input("Выберете раздел: "))
        except ValueError:
            print('Это не целое число. Попробуйте снова...')
            logg.error_enter()
            return start()

        if token == 1:
            print("РАЦИОНАЛЬНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню\n")
            logg.next_step()
            try:
                token2 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не число. Попробуйте снова...')
                logg.error_enter()
                return start()

            if token2 == 1:
                r1 = excep.take_value()
                r2 = excep.take_value()
                model_sum.init(r1, r2)
                result = model_sum.summa()
                logg.sum_log(r1, r2, result)
                print(result)
                return result


            elif token2 == 2:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_sub.init(r1, r2)
                result = model_sub.subtraction()
                logg.sub_log(r1, r2, result)
                print(result)
                return result

            elif token2 == 3:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_mult.init(r1, r2)
                result = model_mult.multiplication()
                logg.mult_log(r1, r2, result)
                print(result)
                return result

            elif token2 == 4:
                print("ДЕЛЕНИЕ ЧИСЛА")
                print("1. '/' - обычное деление")
                print("2. '//' - целочисленное деление")
                print("3. '%' - остаток от деления")
                print("0. Вернуться в главное меню\n")
                try:
                    token3 = int(input("Выберете операцию: "))
                except ValueError:
                    print('Это не целое число. Попробуйте снова...')
                    logg.error_enter()
                    return start()

                if token3 == 1:
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    try:
                        result = model_div.div1()
                        logg.div_log1(r1, r2, result)
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('Делить на ноль нельзя')
                        logg.error_enter()
                        return start()



                elif token3 == 2:
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    try:
                        result = model_div.division()
                        logg.div_log2(r1, r2, result)
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('Делить на ноль нельзя')
                        logg.error_enter()
                        return start()
                elif token3 == 3:
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    try:
                        result = model_div.div2()
                        logg.div_log3()
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('Делить на ноль нельзя')
                        logg.error_enter()
                        return start()
                elif choice3 == 0:
                    start()

            elif token2 == 5:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_pow.init(r1, r2)
                result = model_pow.exponentiation()
                logg.pow_log(r1, r2, result)
                print(result)
                return result

            elif token2 == 6:

                r1 = excep.take_value()
                model_sqrt.init(r1)
                result = model_sqrt.root()
                logg.sgrt_log(r1, result)
                print(result)
                return result

            elif token2 == 0:
                start()
            else:
                print("Ой! Ошибка ввода")
                logg.error_enter()
                start()

        if token == 2:
            print("КОМПЛЕКСНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню")
            try:
                token4 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не целое число. Попробуйте снова...')
                logg.error_enter()
                return start()

            if token4 == 1:
                c1 = compl.init_complex()
                c2 = compl.init_complex()
                model_sum.init(c1, c2)
                result = model_sum.summa()
                logg.sum_log(c1, c2, result)
                print(result)
                return result


            elif token4 == 2:

                c1 = compl.init_complex()
                c2 = compl.init_complex()
                model_sub.init(c1, c2)
                result = model_sub.subtraction()
                logg.sub_log(c1, c2, result)
                print(result)
                return result

            elif token4 == 3:

                c1 = compl.init_complex()
                c2 = compl.init_complex()
                model_mult.init(c1, c2)
                result = model_mult.multiplication()
                logg.mult_log(c1, c2, result)
                print(result)
                return result

            elif token4 == 4:

                c1 = compl.init_complex()
                c2 = compl.init_complex()
                model_div.init(c1, c2)
                try:
                    result = model_div.div1()
                    logg.div_log(c1, c2, result)
                    print(result)
                    return result
                except ZeroDivisionError:
                    print('Делить на ноль нельзя')
                    logg.error_enter()
                    return start()

            elif token4 == 5:

                c1 = compl.init_complex()
                c2 = compl.init_complex()
                model_pow.init(c1, c2)
                result = model_pow.exponentiation()
                logg.pow_log(c1, c2, result)
                print(result)
                return result

            elif token4 == 6:

                c1 = compl.init_complex()
                result = model_sqrt.root(c1)
                logg.sgrt_log(c1, result)
                print(result)
                return result

            elif token4 == 0:
                start()

            else:
                print("Ой! Ошибка ввода")
                logg.error_enter()
                start()

        if token == 0:
            print('До скорых встреч!')
            quit()


start()