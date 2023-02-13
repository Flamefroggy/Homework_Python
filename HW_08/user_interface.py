from database import (academic_discipline, tearcher_work, student_one_discipline, student_all_discipline, student_choose_discipline)
import controller


def tearcher():
    print("---УЧИТЕЛЬ---")
    print('По какому предмету хотите поставить отметку?')
    for i in range(len(academic_discipline)):
        print(f"{i + 1}. {academic_discipline[i]}")
    disc = int(input("Ваш выбор: ")) - 1
    tearcher_work(disc)
    print('------------')
    print('1. Выбрать другой предмет')
    print('2. Вернуться в меню выбора пользователя')
    menu = 0
    while menu != 1 or menu != 2:
        menu = int(input("Ваш выбор: "))
        if menu == 1:
            tearcher()
            break
        elif menu == 2:
            controller.initial()
            break
        else:
            print("Повторите ввод")


def student():
    print("---УЧЕНИК---")
    stud_name = input("Введите фамилию: ")
    print("1. Посмостреть оценки по предмету")
    print("2. Посмотреть все оценки")
    student_choose = int(input('Ваш выбор: '))
    if student_choose == 1:
        discip = student_choose_discipline()
        list_mark = student_one_discipline(stud_name, discip)
    elif student_choose == 2:
        list_mark = student_all_discipline(stud_name)
    else:
        controller.initial()
    if len(list_mark) > 0: print(list_mark)