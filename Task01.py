# 1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# **Input:**

# n = 700

# m = 750

# **Output:**

# 2
# n = 700
# m = 750
# days = m // n + (m % n > 0)
# print(days)
dist = int(input('Сколько машина пиоезжает за день: '))
total = int(input('Сколько надо проехать: '))

print(f'Машине понадобится {int(total + dist - 0.1)//dist} дней')
# print(f'Машине понадобится {int(total//dist + (total%dist > 0} дней') Второй способ решения 