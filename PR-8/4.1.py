from random import *

# Ввод размерности матрицы
strok = int(input('Введите количество строк: '))
stolb = int(input('Введите количество столбцов: '))

# Генерация матрицы случайными числами
a = []
for i in range(strok):
    b = []
    for j in range(stolb):
        b.append(randint(0, 51))
    a.append(b)

# Вывод исходной матрицы
print('Исходная матрица:')
for i in range(strok):
    for j in range(stolb):
        print(a[i][j], end=' ')
    print()

# Нахождение строки с наибольшей суммой элементов
max_sum = 0
max_row = None
min_sum = 10000000
min_row = None

for i in range(strok):
    row_sum = sum(a[i])
    if row_sum > max_sum:
        max_sum = row_sum
        max_row = a[i]
    if row_sum < min_sum:
        min_sum = row_sum
        min_row = a[i]

# Вывод строк с наибольшей и наименьшей суммой элементов
print('Строка с наибольшей суммой элементов:')
print(max_row)
print('Сумма элементов:', max_sum)

print('Строка с наименьшей суммой элементов:')
print(min_row)
print('Сумма элементов:', min_sum)