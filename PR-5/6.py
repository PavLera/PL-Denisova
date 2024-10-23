s = input("Введите строку: ")

s1 = s.replace("а", "")
count = len(s) - len(s1)

print("Новая строка:", s1)
print("Количество удаленных символов:", count)