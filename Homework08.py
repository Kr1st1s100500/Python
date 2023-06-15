# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Ширина: '))
lenght = int(input('Длинна: '))
piece = int(input('Кусок: '))

if width*lenght > piece and (piece%width == 0 or piece%lenght == 0):
    print('YES')
else:
    print('NO')