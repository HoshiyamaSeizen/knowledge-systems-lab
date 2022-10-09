from tkinter import *
from tools import *

def astigmatismTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест на цветовосприятие")
    newWindow.geometry("1000x700")
    window.resizable(False, False)
    Label(newWindow, text ="Тест на цветовосприятие", font=("Arial", 25)).grid(row=0, pady=(40, 20), padx=(100, 0))

    err = Label(newWindow, text = "").grid(row = 2, padx=(100, 0))
    Label(newWindow, text = "Как много различных цветов вы видите? ").grid(row = 3, padx=(100, 0))
    entry = Entry(newWindow).grid(row = 3, column = 1, padx=(100, 0))

    Button(window, text="Завершить", width=25, command= calculate).grid(row=4, padx=(100, 0), pady=(100, 0))

def calculate():
    pass