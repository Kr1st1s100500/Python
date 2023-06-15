# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
 
 
# number = int(input("Введите число: "))
# i = 3
# fib_1 = 0
# fib_2 = 1
# answer = fib_1 + fib_2
# while answer < number:
#     fib_1 = fib_2
#     fib_2 = answer
#     answer = fib_1 + fib_2
#     i = i + 1
   
# print(answer)
# if number == answer:
#     print(i)
# else:
#     print(-1) 
      
# number = int(input())
# n1=0
# n2=1
# position=2
# while n2<number:
#     n1,n2 = n2, n1+n2
#     position+=1
# if n2!=number:
#     print("-1")
# else:
#     print(position) # Второй способ решения


limit = int(input('Введите число: '))

fib_1 = 0
fib_2 = 1
position = 2

while fib_2 < limit:
    fib_2, fib_1 = fib_2 + fib_1, fib_2
    position += 1
    
if limit ==fib_2:
    print(f'В последовательности Фиббоначи число {fib_2} стоит на {position} позиции')
else:
   print(-1) 
#    Третий способ решения задачи