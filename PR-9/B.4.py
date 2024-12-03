def is_prime(n, i=2):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

n = int(input("Введите натуральное число n: "))
if is_prime(n) == 1:
    print("YES")
else:
    print("NO")