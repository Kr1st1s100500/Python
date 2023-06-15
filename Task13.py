# Напишите программу, которая на вход принимает строку.
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

import random

my_list = [random.randint(0,10) for _ in range (20)]
print(my_list)
counter = {} #создаем словарь

for item in my_list: # проходимся по элементам нашего списка
    counter[item] = counter.get(item, 0) + 1 # чему равен ключ
    print(item if counter.get(item) < 2 else (str(item) + '_' + str(counter.get(item) - 1)), end=' ')
    