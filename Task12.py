# Дан список, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов в списка,
# больших предыдущего (элемента с предыдущим номером).

from random import randint
lis = []
lens = 10
for i in range(10):
    lis.append(randint(0, 10))
print(lis)
k = 0
for i in range(len(lis)):
    if