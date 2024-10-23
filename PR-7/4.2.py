import math
def circle(x, y, a, b, R):
    distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    return distance < R

a = int(input("Введите координату x центра окружности: "))
b = int(input("Введите координату y центра окружности: "))
R = int(input("Введите радиус окружности: "))

p1 = int(input("Введите координату x точки P: "))
p2 = int(input("Введите координату y точки P: "))
f1 = int(input("Введите координату x точки F: "))
f2 = int(input("Введите координату y точки F: "))
l1 = int(input("Введите координату x точки L: "))
l2 = int(input("Введите координату y точки L: "))

count = 0
if circle(p1, p2, a, b, R):
    count += 1
if circle(f1, f2, a, b, R):
    count += 1
if circle(l1, l2, a, b, R):
    count += 1

print(f"Количество точек, лежащих внутри окружности: {count}")
