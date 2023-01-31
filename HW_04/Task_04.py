# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и вывести многочлен степени k.

from random import randint

k = int(input("Введите степень k: "))
for i in range(k, 0, -1):
    factor = randint(1, 100)
    if factor == 1:
        factor = ""
    else:
        if i != 1:
            factor = f"{factor}*x^{i} +"
        else:
            factor = f"{factor}*x +"
        
    print (factor, end=" ")

print(f"{randint(1, 100)} = 0")