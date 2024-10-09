text = input("Введите строку: ")

new_text = text.replace("а", "")
deleted_count = len(text) - len(new_text)

print("Новая строка:", new_text)
print("Количество удаленных символов:", deleted_count)