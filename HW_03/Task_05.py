# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
def fibo(n):
    list_fn = [0, 1]
    for i in range(2, n + 1):
        list_fn.append(list_fn[i - 1] + list_fn[i - 2])
    for j in range(n):
        list_fn.insert(0, list_fn[1] - list_fn[0])
    return list_fn

print(fibo(n))