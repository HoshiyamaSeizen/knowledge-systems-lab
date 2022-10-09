from tkinter import *
from perception import perceptionTest
from daltonism import daltonismTest
from astigmatism import astigmatismTest
from amsler import amslerTest

if __name__ == "__main__":
    window = Tk()
    window.geometry("600x300")
    window.resizable(False, False)
    window.title("Проверка зрения")

    res1 = Label(window, text ="Не проверено")
    res1.grid(row=1, column=1, padx=(0, 0))
    Button(window, text="Тест на цветовосприятие", width=25, command= lambda: perceptionTest(window, res1)).grid(row=0, column=0, padx=(100, 0), pady=(30, 0))
    Label(window, text ="Результат на цветовосприятие: ").grid(row=1, column=0, padx=(100, 0))

    res2 = Label(window, text ="Не проверено")
    res2.grid(row=3, column=1, padx=(0, 0))
    Button(window, text="Тест на дальтонизм", width=25, command= lambda: daltonismTest(window, res2)).grid(row=2, column=0, padx=(100, 0), pady=(20, 0))
    Label(window, text ="Результат на дальтонизм: ").grid(row=3, column=0, padx=(100, 0))

    res3 = Label(window, text ="Не проверено")
    res3.grid(row=5, column=1, padx=(0, 0))
    Button(window, text="Тест на астигматизм", width=25, command= lambda: astigmatismTest(window, res3)).grid(row=4, column=0, padx=(100, 0), pady=(20, 0))
    Label(window, text ="Результат на астигматизм: ").grid(row=5, column=0, padx=(100, 0))

    res4 = Label(window, text ="Не проверено")
    res4.grid(row=7, column=1, padx=(0, 0))
    Button(window, text="Тест Амслера", width=25, command= lambda: amslerTest(window, res4)).grid(row=6, column=0, padx=(100, 0), pady=(20, 0))
    Label(window, text ="Результат теста Амслера: ").grid(row=7, column=0, padx=(100, 0))

    window.mainloop()