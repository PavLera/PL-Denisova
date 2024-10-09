n = int(input("Введите натуральное число n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("n! =", factorial)