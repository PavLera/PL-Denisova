text = input("Введите строку: ")

new_text = text.replace("а", "о")
count_replacements = len(text) - len(new_text)

print("Новая строка:", new_text)
print("Количество замен:", count_replacements)
print("Количество символов:", len(text))