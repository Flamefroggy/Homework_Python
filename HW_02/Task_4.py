# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input("Введите натуральное число: "))
number_list=[]
for i in range(1,n+1):
    number_list.append(i)
sum = 0
for i in range(len(number_list)):
    if i % 2 != 0:
        sum += number_list[i]
print(number_list)
print(sum)
