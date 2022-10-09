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

    err = Label(newWindow, text = "", fg='red')
    err.grid(row = 2, padx=(100, 0))

    entries = []
    # Такие штуки надо для каждого вопроса
    Label(newWindow, text = "Вопрос 1").grid(row = 3, padx=(100, 0))
    entry = Entry(newWindow)
    entries.append(entry)
    entry.grid(row = 3, column = 1)

    Label(newWindow, text = "Вопрос 2").grid(row = 4, padx=(100, 0))
    entry = Entry(newWindow)
    entries.append(entry)
    entry.grid(row = 4, column = 1)
    ###

    Button(newWindow, text="Завершить тест", width=25, command= lambda: calculate(entries, resLabel, err, newWindow)).grid(row=4, padx=(100, 0), pady=(100, 0))

def calculate(entries, label, errLabel, window):
    for entry in entries:
        print(entry.get())
    if(False): # Вывод ошибки если значение не подходит
        errLabel.config(text="Некорректное значение" if err else "") 
    label.config(text="Ответ")
    label.config(fg="green")
    window.destroy()