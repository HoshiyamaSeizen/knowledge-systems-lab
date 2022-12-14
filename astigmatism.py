from tkinter import *
from tkinter import ttk
from tools import *

countAnswers = 3
current = None
answers = []
value_inside = None

def astigmatismTest(window, resLabel):
    newWindow = Toplevel(window)
    newWindow.title("Тест на астигматизм")
    newWindow.geometry("900x900")
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
    global value_inside
    global answers

    err = False
    if(current!= 1 and value_inside and value_inside.get() != "Выберите значение"):
        answers.append(value_inside.get())
    elif(current != 1): err = True

    errLabel.config(text="Некорректное значение" if err else "")
    if(err): return

    if(current == countAnswers + 1): return calculate(window, resLabel)

    for widget in frame.winfo_children():
        widget.destroy()

    img = loadImage(f"./assets/a{current}.jpg", 300, 300) # Для каждого изображения свой размер
    if (current == 2):
        img = loadImage(f"./assets/a2.jpg", 323, 72)
    panel.config(image = img)
    panel.image = img
    
    question = ""
    if current == 1:
        question = "Закройте один глаз, сделайте 3-5 шагов назад от монитора и посмотрите на круг.\nСтановятся ли некоторые из линий темнее, чем другие?"
    if current == 2:
        question = "Закройте один глаз, а затем другой.\nВидите ли вы линованные квадраты разными оттенками?"
    if current == 3:
        question = "На данной картинке лучи с определённого момента начнут сливаться.\n Граница четкой видимости лучей, которую вы видите, представляет собой эллипс (не является правильной окружностью)?"
    
    Label(frame, text= f"Вопрос {current}:\n{question}").pack()

    options_list = ["Да", "Нет"]
    value_inside = StringVar(frame)

    value_inside.set("Выберите значение")
    currentEntry = OptionMenu(frame, value_inside, *options_list)
    currentEntry.pack()

    current+=1


def calculate(window, label):
    print(answers)
    if (("#".join(answers)).count("Да") == 3):
        label.config(text="У вас астигматизм")
        label.config(fg="red") 
    if (("#".join(answers)).count("Да") == 2):
        label.config(text="С большой вероятностью у вас астигматизм")
        label.config(fg="orange")
    if (("#".join(answers)).count("Да") == 1):
        label.config(text="Возможно у вас астигматизм")
        label.config(fg="black")
    if (("#".join(answers)).count("Да") == 0):
        label.config(text="У вас нет астигматизма")
        label.config(fg="green")
    answers.clear()
    window.destroy()