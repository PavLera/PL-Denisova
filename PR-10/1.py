'''n = 4
a = []
#Заполняем массив элементами из файла
file_vvod = open('DenisovaValeriaPavlovna_YB-42_vvod.txt')
for i in file_vvod:
    n1 = int(i)
    a.append(n1)
a = [a] * n
for i in a:
    print(*i)

for i in range(n):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

print('Изменённый массив')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

print('-'*8)
#Добавляем результат в файл
file_vivod = a
file_v = open('../../PycharmProjects/VSUET/DenisovaValeriaPavlovna_YB-42_vivod.txt','w')
file_v.write(str(file_vivod))
file_v.close()
for i in a:
    print(*i)'''
n = 4
a = []
#Заполняем массив элементами из файла
with open("DenisovaValeriaPavlovna_YB-42_vvod.txt") as file:
    for line in file:
        arr = [int(x.strip()) for x in line.split()]
        a.append(arr)

print('Исходный массив:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
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
        print(a[i][j], end=' ')
    print()

#Добавляем результат в файл
file_vivod = a
with open('DenisovaValeriaPavlovna_YB-42_vivod.txt', 'w') as file_v:
    for row in a:
        file_v.write(' '.join(map(str, row)) + '\n')