def sum(number):
    digit = filter(lambda x: x.isdigit(), str(number))
    return sum(map(int, list(digit)))

number = input("Введите вещественное число: ")

print(f"Сумма цифр в числе: {sum(number)}")