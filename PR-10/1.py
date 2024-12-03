n = 4
a = []
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

file_vivod = a
with open('DenisovaValeriaPavlovna_YB-42_vivod.txt', 'w') as file_v:
    for row in a:
        file_v.write(' '.join(map(str, row)) + '\n')