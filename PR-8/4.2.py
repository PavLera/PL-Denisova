from random import *

n = int(input('Введите кол-во строк и столбцов'))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(-51, 51))
    a.append(b)

# вывод массива
print('Исходный массив')
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()

for i in range(n):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

print('Изменённый массив')
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()



