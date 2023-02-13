from user_interface import (tearcher, student)


def initial():
    choose = 0
    while choose != 3:
        print("_____________________")
        print("+++ ГЛАВНОЕ МЕНЮ +++")
        print("1. Учитель")
        print("2. Ученик")
        print("3. Выход")
        choose = int(input("Вам куда? "))
        if choose == 1:
            tearcher()
        elif choose == 2:
            student()
        else:
            break