number = input('Введите любое вещественное число: ')

list_num = list(map(int, (i for i in number if i.isdigit())))

sum_digit = sum(list_num)

print(f'Исходное число: {number}')
print(f'Сумма его чисел = {sum_digit}')