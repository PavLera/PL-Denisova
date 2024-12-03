from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import requests
import json

def repo():
    username = username_entry.get()
    repo_name = repo_entry.get()

    response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}")
    response.raise_for_status()
    repo_data = response.json()

    info = {
        "company": repo_data.get("owner").get("company"),
        "created_at": repo_data.get("created_at"),
        "email": repo_data.get("email"),
        "id": repo_data.get("owner").get("id"),
        "name": repo_data.get("name"),
        "url": repo_data.get("owner").get("html_url")
    }

    # Сохранение Json файла
    file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    with open(file, "w") as f:
        json.dump(info, f)
    messagebox.showinfo("Успех", f"Информация о репозитории записана в файл {file}")

window = Tk()

window.title("Информация о репозитории GitHub")
window.geometry('400x100')

username_label = Label(window, text="Имя пользователя на GitHub:")
username_label.grid(column=0, row=0)
username_entry = Entry(window, width=30)
username_entry.grid(column=1, row=0)

repo_label = Label(window, text="Имя репозитория:")
repo_label.grid(column=0, row=1)
repo_entry = Entry(window, width=30)
repo_entry.grid(column=1, row=1)

get_button = Button(window, text="Получить информацию", command=repo)
get_button.grid(column=1, row=2)

window.mainloop()