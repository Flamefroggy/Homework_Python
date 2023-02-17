from models import str_to_list, operations


def solve_little(task):
    task = str_to_list(task)
    task = operations(task, 0)
    task = operations(task, 2)
    return task[0]


def solve_task(task_str):
    right = task_str.find(')')
    while right > 0:
        left = task_str[:right].rfind('(')
        task = task_str[left + 1:right]
        task = solve_little(task)
        if right == len(task_str): right -= 1
        task_str = task_str[:left] + str(task) + task_str[right + 1:]
        right = task_str.find(')')
    task = solve_little(task_str)
    return task