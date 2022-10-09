from tkinter import *
from tkinter import ttk
from tools import *

current = None

def daltonismTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест на Дальтонизм")
    newWindow.geometry("900x600")
    window.resizable(False, False)
    Label(newWindow, text ="Тест на дальтонизм", font=("Arial", 25)).grid(row=0, pady=(40, 20), padx=(100, 0))

    global current
    current = 1

    img = loadImage("./assets/d1.jpg", 500, 300)
    panel = Label(newWindow, image=img)
    panel.image = img
    panel.grid(row=1, padx=(100, 0))

    frame = Frame(newWindow)
    frame.grid(row=2)

    next(panel, frame)  

    Button(newWindow, text="Дальше", width=25, command= lambda: next(panel, frame)).grid(row=4, padx=(100, 0), pady=(100, 0))  


def next(panel, frame):
    global current
    if(current == 14): return calculate()
    img = loadImage(f"./assets/d{current}.jpg", 500, 300)
    panel.config(image = img)
    panel.image = img

    for widget in frame.winfo_children():
        widget.destroy()
    
    Label(frame, text=f"Question {current}").pack()

    current+=1


def calculate():
    pass