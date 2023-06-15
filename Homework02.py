# Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input('Введите число: ')

sum_ = 0
for i in range(len(number)):
    sum_ += int(number[i])
    
print(sum_)