from tkinter import *
from tools import *

def perceptionTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест на цветовосприятие")
    newWindow.geometry("900x600")
    window.resizable(False, False)
    Label(newWindow, text ="Тест на цветовосприятие", font=("Arial", 25)).grid(row=0, pady=(40, 20), padx=(100, 0))

    img = loadImage("./assets/spectr.jpg", 300, 300)
    panel = Label(newWindow, image=img)
    panel.image = img
    panel.grid(row=1, padx=(100, 0))

    err = Label(newWindow, text = "", fg='red')
    err.grid(row = 2, padx=(100, 0))
    Label(newWindow, text = "Как много различных цветов вы видите? ").grid(row = 3, padx=(100, 0))
    entry = Entry(newWindow)
    entry.grid(row = 3, column = 1)

    Button(newWindow, text="Завершить тест", width=25, command= lambda: calculate(entry.get(), resLabel, err, newWindow)).grid(row=4, padx=(100, 0), pady=(100, 0))

def calculate(value, label, errLabel, window):
    if(not value.isnumeric()):
        return errLabel.config(text="Нужно ввести положительное число")
    value = int(value)
    if(value <= 0):
        errLabel.config(text="Нужно ввести положительное число")
    elif(value > 39):
        errLabel.config(text="Здесь не так много цветов")
    elif(value < 20): 
        label.config(text="Менее 20 цветов. Вы дихромат")
        label.config(fg="green")
        window.destroy()
    elif(value < 32): 
        label.config(text="От 20 до 32 цветов. Вы – трихромат")
        label.config(fg="green")
        window.destroy()
    else: 
        label.config(text="От 32 до 39 цветов. Вы – тетрахромат")
        label.config(fg="green")
        window.destroy()