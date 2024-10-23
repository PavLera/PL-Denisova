s = input("Введите строку: ")
count = 0

while 'а' in s:
    s = s.replace("а", "о", 1)
    count += 1

print("Новая строка:", s)
print("Количество замен:", count)
print("Количество символов:", len(s))
