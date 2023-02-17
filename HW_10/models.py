oper = ['/', '*', '+', '-']


def str_to_list(task):
    lst = []
    count = 0
    for i in range(len(task)):
        if task[i] in oper:
            lst.append(int(task[count:i]))
            lst.append(task[i])
            count = i + 1
    lst.append(int(task[count:len(task)]))
    print(lst)
    return lst


def operations(task, znak):
    i = 0
    while i < len(task):
        if task[i] == oper[znak] or task[i] == oper[znak + 1]:
            task[i - 1] = calculation(task[i - 1], task[i + 1], task[i])
            task.pop(i + 1)
            task.pop(i)
            i = 0
        i += 1
    return task


def calculation(num1, num2, operation):
    result = 1
    if operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    return result