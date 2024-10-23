m = int(input("Введите количество элементов в списке: "))
a = []
for i in range(m):
    b = int(input("Введите элементы списка:"))
    a.append(b)

a2 = []
for num in a:
    if num % 2 != 0:
        a2.append(num)
if len(a2) > 0:
    a2.sort(reverse=True)
    print("Отфильтрованные нечетные числа в порядке убывания:", a2)
else:
    print("Чисел нечетного типа нет")