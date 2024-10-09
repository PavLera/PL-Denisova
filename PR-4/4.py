n = int(input("Введите количество чисел: "))
summa = 0
for i in range(n):
    chislo = int(input("Введите число: "))
    summa += chislo
print("Сумма чисел:", summa)