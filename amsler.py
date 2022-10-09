from tkinter import *
from tools import *

def amslerTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест Амслера")
    newWindow.geometry("900x600")
    window.resizable(False, False)
    Label(newWindow, text ="Тест Амслера", font=("Arial", 25)).grid(row=0, pady=(40, 20), padx=(100, 0))

    img = loadImage("./assets/amsler.jpg", 300, 301)
    panel = Label(newWindow, image=img)
    panel.image = img
    panel.grid(row=1, padx=(100, 0))

    err = Label(newWindow, text="", fg='red')
    err.grid(row=2, padx=(100, 0))

    value_inside_1 = StringVar(newWindow)
    value_inside_1.set("Выберете ответ")
    value_inside_2 = StringVar(newWindow)
    value_inside_2.set("Выберете ответ")
    value_inside_3 = StringVar(newWindow)
    value_inside_3.set("Выберете ответ")
    values = [value_inside_1, value_inside_2, value_inside_3]
    options = ("Да", "Нет")

    Label(newWindow, text = "Все ли линии сетки прямые и ровные?").grid(row = 3, padx=(100, 0))
    entry = OptionMenu(newWindow, value_inside_1, *options)
    entry.grid(row = 3, column = 1)

    Label(newWindow, text="Все ли квадраты решетки одинакового размера?").grid(row=4, padx=(100, 0))
    entry = OptionMenu(newWindow, value_inside_2, *options)
    entry.grid(row=4, column=1)

    Label(newWindow, text="Нет ли зон, где рисунок искажается, затуманивается, обесцвечивается?").grid(row=5, padx=(100, 0))
    entry = OptionMenu(newWindow, value_inside_3, *options)
    entry.grid(row=5, column=1)

    Button(newWindow, text="Завершить тест", width=25, command=lambda: calculate(values, resLabel, err,  newWindow)).grid(row=6, padx=(100, 0), pady=(20, 0))

def calculate(values, label, errLabel, window):
    vals = []
    for val in values:
        vals.append(val.get())
    if (("#".join(vals)).count("Нет") == 3):
        label.config(text="У вас макулодистрофия")
        label.config(fg="red")
        window.destroy()
    elif (("#".join(vals)).count("Нет") == 2 and ("#".join(vals)).count("Да") == 1):
        label.config(text="С большой вероятностью у вас макулодистрофия")
        label.config(fg="orange")
        window.destroy()
    elif (("#".join(vals)).count("Нет") == 1 and ("#".join(vals)).count("Да") == 2):
        label.config(text="Возможно у вас макулодистрофия")
        label.config(fg="black")
        window.destroy()
    elif (("#".join(vals)).count("Да") == 3):
        label.config(text="У вас нет макулодистрофии")
        label.config(fg="red")
        window.destroy()
    else:
        errLabel.config(text="Ответьте на все вопросы")
