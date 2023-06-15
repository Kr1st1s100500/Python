# Дан список чисел. Пределите, сколько в нем встречается различных чисел.
# from random import randint
import random

my_list = []
for _ in range(10):
    my_list.append(random.randint(0, 10))
print(my_list)
    
my_list = set(my_list)
print(my_list)
print(len(my_list)) 
#  Проверка каждого значения
# uniq_list = []
# for item in my_list:
#     if item not in uniq_list:
#         uniq_list.append(item)
# print(uniq_list)
# print(set(my_list)) в фигурных скобках вывод 
# print(list(set(my_list))) в квадратных