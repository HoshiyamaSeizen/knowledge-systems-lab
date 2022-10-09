from tkinter import *
from tkinter import ttk
from tools import *

countAnswers = 3
current = None
currentEntry = None
answers = []

def astigmatismTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест на астигматизм")
    newWindow.geometry("900x600")
    window.resizable(False, False)
    Label(newWindow, text ="Тест на астигматизм", font=("Arial", 25)).grid(row=0, pady=(40, 20), padx=(100, 0))

    global current
    current = 1

    panel = Label(newWindow)
    panel.grid(row=1, padx=(100, 0))

    err = Label(newWindow, text = "", fg='red')
    err.grid(row = 2, padx=(100, 0))

    frame = Frame(newWindow)
    frame.grid(row=3)

    next(panel, frame, err, newWindow, resLabel)

    Button(newWindow, text="Дальше", width=25, command= lambda: next(panel, frame, err, newWindow, resLabel)).grid(row=4, padx=(100, 0), pady=(100, 0))  


def next(panel, frame, errLabel, window, resLabel):
    global current
    global currentEntry
    global answers

    if(current <= countAnswers):
        img = loadImage(f"./assets/a{current}.jpg", 300, 300) # Для каждого изображения свой размер
        panel.config(image = img)
        panel.image = img

    err = False
    # Сохранение данных из полей ввода (надо доработать, если там не импуты а чекбоксы или радио-баттоны)
    if(currentEntry):
        # Проверка допустимости ответа, иначе err = True
        answers.append(currentEntry.get())
    ###

    if(current == countAnswers + 1): return calculate(window, resLabel)

    for widget in frame.winfo_children():
        widget.destroy()
    
    Label(frame, text=f"Question {current}").pack() # Текст вопроса

    # Добавление поля для ответа (разные в зависимости от вопроса)
    if(current == 1):
        currentEntry = Entry(frame)
        currentEntry.pack()
    else:
        currentEntry = Entry(frame)
        currentEntry.pack()
    ###

    errLabel.config(text="Некорректное значение" if err else "")

    current+=1


def calculate(window, label):
    print(answers)
    label.config(text="Ответ")
    label.config(fg="green")
    window.destroy()