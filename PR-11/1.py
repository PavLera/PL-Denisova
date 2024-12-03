from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox as ms

def calculate():
    num1 = float(chislo1.get())
    num2 = float(chislo2.get())

    if combobox.get() == '+':
        res = num1 + num2
    if combobox.get() == '-':
        res = num1 - num2
    if combobox.get() == '*':
        res = num1 * num2
    if combobox.get() == '/':
        if num2 == 0:
            ms.showinfo('Результат', 'Нельзя делить на ноль!')
        else:
            res = num1 / num2

    ms.showinfo('Результат', f'Результат:{res}')

def check():
    vibor = []

    if chk1_state.get() == 1:
        vibor.append('Первый вариант')
    if chk2_state.get() == 1:
        vibor.append('Второй вариант')
    if chk3_state.get() == 1:
        vibor.append('Третий вариант')

    if vibor:
        ms.showinfo('Результат', "Вы выбрали: " + ", ".join(vibor))
    else:
        ms.showinfo('Результат', 'Ничего не выбрано')

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text1 = file.read()
            text.delete("1.0", END) # удаляем старый текст
            text.insert("1.0", text1) # добавляем новый текст

root = Tk()

root.title('Денисова Валерия Павловна')
root.geometry('600x300')

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control, width=10)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')

# КАЛЬКУЛЯТОР
chislo1 = Entry(tab1, width=20)
chislo1.grid(column=0, row=1, padx=(80,10))

method_lbl = Label(tab1, text='Выберите действие')
method_lbl.grid(column=1, row=0, pady = (70,0))
methods = ['+', '-', '*', '/']
combobox = Combobox(tab1, values=methods, width=15)
combobox.current(0)
combobox.grid(column=1, row=1, padx=(0, 10))

chislo2 = Entry(tab1, width=20)
chislo2.grid(column=2, row=1)

calc_btn = Button(tab1, text='=', command=calculate)
calc_btn.grid(column=3, row=1, padx=(10, 0))

# ЧЕКБОКСЫ
chk1_state = BooleanVar()
chk1 = Checkbutton(tab2, text='Первый', var = chk1_state)
chk1.pack(pady=(30,0))

chk2_state = BooleanVar()
chk2 = Checkbutton(tab2, text='Второй', var = chk2_state)
chk2.pack(pady=(20, 0))

chk3_state = BooleanVar()
chk3 = Checkbutton(tab2, text='Третий', var = chk3_state)
chk3.pack(pady=(20, 0))

btn_check = Button(tab2, text='Вывод выбранного варианта', command=check)
btn_check.pack(pady=(10, 0))

#ТЕКСТ
text = scrolledtext.ScrolledText(tab3, width=50, height=10)
text.pack(padx=10, pady=30)

text_btn = Button(tab3, text='Загрузить файл', command=open_file)
text_btn.pack(padx=30, pady=5)

tab_control.pack(expand=1, fill='both')
root.mainloop()