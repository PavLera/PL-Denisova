A = int(input("Введите A (числитель первой дроби): "))
B = int(input("Введите B (знаменатель первой дроби): "))
C = int(input("Введите C (числитель второй дроби): "))
D = int(input("Введите D (знаменатель второй дроби): "))

chislit = A * D
znamenat = B * C
def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

delit = nod(chislit, znamenat)
chislit //= delit
znamenat //= delit

print(f"Результат деления дробей: {chislit}/{znamenat}")
