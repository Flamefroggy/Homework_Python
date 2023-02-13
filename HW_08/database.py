academic_discipline = ['Русский язык', 'Математика', 'Информатика']


def tearcher_work(discipline):
    path = academic_discipline[discipline] + '.txt'
    try:
        with open(path, 'r', encoding='windows-1251') as file:
            lines = file.readlines()
    except:
        with open(path, 'w+', encoding='windows-1251') as file:
            lines = file.readlines()
    print("---Список учеников---")
    print("Укажите порядковый номер ученика: ")
    i = -1
    for i in range(len(lines)):
        lst = lines[i].split()
        print(f"{i + 1}. {lst[0]}")
    print(f"{i + 2}. Ученика нет. Добавить. ")
    count = input("Ваш выбор: ")
    while not (count.isdigit()) or int(count) > i + 2:
        count = input("Повторите ввод: ")
    if int(count) == i + 2 or (int(count) - 2 == -1 and i == -1):
        student_add(discipline)
    else:
        mark_add(discipline, int(count))


def student_add(discipline):
    print("---Новый ученик---")
    student = input("Укажите фамилию ученика: ")
    mark = input("Какую отметку вы хотите поставить: ")
    path = academic_discipline[discipline] + '.txt'
    with open(path, 'a', encoding="windows-1251") as file:
        file.write(f"{student} {mark}\n")
    return


def mark_add(discipline, student):
    path = academic_discipline[discipline] + '.txt'
    with open(path, 'r+', encoding='windows-1251') as file:
        lines = file.readlines()
    i = 1
    new_lines = str()
    for line in lines:
        if i == student:
            lst = line.split()
            mark = input(f"Какую оценку ставим {lst[0]}: ")
            lst.append(mark)
            str_lst = " ".join(lst)
            print(str_lst)
            line = str_lst + '\n'
        new_lines = new_lines + line
        i += 1
    with open(path, 'w') as file:
        file.write(new_lines)


def student_choose_discipline():
    for i in range(len(academic_discipline)):
        print(f"{i + 1}. {academic_discipline[i]}")
    return int(input("Какой предмет? "))


def student_all_discipline(student_name):
    lst_mark = str()
    for i in range(len(academic_discipline)):
        path = academic_discipline[i] + ".txt"
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                temp = line.split()
                if temp[0] == student_name:
                    lst_mark = lst_mark + academic_discipline[i] + ' - - ' + line
        except:
            lst_mark = lst_mark + academic_discipline[i] + '- - ' + student_name + " нет оценок"
    return lst_mark


def student_one_discipline(student_name, discipline):
    path = academic_discipline[discipline - 1] + '.txt'
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except:
        lines = ""
    if lines == "":
        print(f"по предмету '{academic_discipline[discipline]}' нет оценок")
    else:
        lst_mark = str()
        for line in lines:
            temp = line.split()
            if temp[0] == student_name:
                for i in range(1, len(temp)):
                    lst_mark = lst_mark + temp[i] + ' '

    return lst_mark