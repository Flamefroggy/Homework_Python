# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2
list = []
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
    else:
        i+= 1
print(f"Простые множители: {list}")