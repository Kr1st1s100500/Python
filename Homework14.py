#  Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#  не превосходящие числа N.

n = abs(int(input('Введите число N ')))
num = 0
p = 2
for i in range(n):
    if num != 1:
        p = p ** i
        if p <= n:
            print(p, end=' ')
            p = 2
        else:
            num = 1
    else:
        i = n