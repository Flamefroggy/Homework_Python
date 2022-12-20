# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

n = int(input("Введите натуральное число, большее 3: "))
number_list=[]
for i in range(-n,n+1):
    number_list.append(i)
in_check = [0,2,7,1,9]
product = 1
for i in in_check:
    product *= number_list[i]
print(number_list)
print(in_check)
print(f'Произведение элементов на искомых индексах равно {product}')