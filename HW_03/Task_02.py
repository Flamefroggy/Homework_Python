# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    list.append(int(input(f"Введите число №{i+1}: ")))
    i += 1

list2 = []
for i in range(len(list)):
    while i < len(list) / 2 and n > len(list) / 2:
        n = n - 1
        p = list[i] * list[n]
        list2.append(p)
        i += 1

print("Ответ: ", list)
print("Ответ: ", list2)