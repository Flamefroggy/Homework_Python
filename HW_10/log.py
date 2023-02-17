from datetime import datetime


def logging(id, task):
    now = datetime.now()
    with open('log.txt', 'a') as file:
        text = str(now) + "--" + str(id) + " " + task + '\n'
        file.write(text)