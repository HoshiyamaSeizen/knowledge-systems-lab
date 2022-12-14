from tkinter import *
from tkinter import ttk
from tools import *

countAnswers = 13
current = None
currentEntry = None
answers = []
value_inside = None


def daltonism_test(window, resLabel):
    new_window = Toplevel(window)
    new_window.title("Тест на Дальтонизм")
    new_window.geometry("900x600")
    window.resizable(False, False)
    Label(new_window, text="Тест на дальтонизм", font=("Arial", 25)).grid(row=0, pady=(10, 10), padx=(100, 0))

    global current
    current = 1

    panel = Label(new_window)
    panel.grid(row=1, padx=(100, 0))

    err = Label(new_window, text="", fg='red')
    err.grid(row=2, padx=(100, 0))

    frame = Frame(new_window)
    frame.grid(row=3)

    next(panel, frame, err, new_window, resLabel)

    Button(new_window, text="Дальше", width=25, command=lambda: next(panel, frame, err, new_window, resLabel)).grid(row=4, padx=(100, 0), pady=(100,0))


def next(panel, frame, errLabel, window, resLabel):
    global current
    global currentEntry
    global answers
    global value_inside

    err = False
    input_questions = [1, 2, 4, 6, 7, 8, 9, 11, 12]
    one_choice_questions = [3]
    multiple_choice_questions = [5, 10, 13]
    if currentEntry or value_inside:
        if currentEntry and (current - 1) in input_questions:
            ans = currentEntry.get()
            if(not ans.isnumeric()): err = True
            else: answers.append(ans)
        elif value_inside and (current - 1) in one_choice_questions:
            ans = value_inside.get()
            if(ans == "Выберите значение"): err = True
            else: answers.append(ans)
        elif (current - 1) in multiple_choice_questions:
            selected = currentEntry.curselection()
            answers.append(selected)

    errLabel.config(text="Некорректное значение" if err else "")
    if(err): return

    if current == countAnswers + 1:
        calculate(window, resLabel)
        answers.clear()
        return

    for widget in frame.winfo_children():
        widget.destroy()
    
    img = loadImage(f"./assets/d{current}.jpg", 500, 300)
    panel.config(image=img)
    panel.image = img

    Label(frame, text=f"Вопрос {current}: Что вы видите на рисунке?").pack()
    if current in input_questions:
        currentEntry = Entry(frame)
        currentEntry.pack()
    elif current in one_choice_questions:
        options_list = []
        if current == 3:
            options_list.extend(['Круг', 'Треугольник', 'Квадрат', 'Только цветные кружочки'])
        value_inside = StringVar(frame)
        value_inside.set("Выберите значение")
        currentEntry = OptionMenu(frame, value_inside, *options_list)
        currentEntry.pack()
    elif current in multiple_choice_questions:
        options_list = []
        if current == 5 or current == 13:
            options_list.extend(['Круг', 'Треугольник', 'Квадрат', 'Только цветные кружочки'])
        if current == 10:
            options_list.extend(['Круг', 'Треугольник', 'Квадрат', 'Два треугольника'])
        value_inside = StringVar(frame)
        value_inside.set("Выберите значение")
        currentEntry = Listbox(frame, selectmode="multiple", height=4)
        for val in options_list:
            currentEntry.insert(END, val)
        currentEntry.pack()

    current += 1


def calculate(window, label):
    right_answers = ['96', '9', 'Треугольник', '13', (0, 1), '5', '9', '136', '30', (0, 1), '36', '9', (0, 1)]
    res = sum(list(map(lambda a, b: a == b, answers, right_answers)))
    res_text = 'Ответ'
    color = "green"
    if res >= 11:
        res_text = "У Вас нет дальтонизма."
        color = 'green'
    if res < 5:
        res_text = 'У Вас дальтонизм.'
        color = 'red'
    elif 5 <= res < 11:
        res_text = 'Возможно у вас дальтонизм.'
        color = 'orange'

    label.config(text=res_text)
    label.config(fg=color)
    window.destroy()
