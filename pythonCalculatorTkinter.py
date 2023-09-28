import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

pencere = tk.Tk()
pencere.title("Calculator-Adem Alperen Arda")
cerceve = tk.Frame(master=pencere, bg='yellow', padx=10)
cerceve.pack()
giris = tk.Entry(master=cerceve, relief=SUNKEN, borderwidth=3, width=30)
giris.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def click(number):
    giris.insert(tk.END, number)


def esit():
    try:
        y = str(eval(giris.get()))
        giris.delete(0,tk.END)
        giris.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Hata", "Syntax Hatası")


def clear():
    giris.delete(0, tk.END)


button_1 = tk.Button(master=cerceve, text='1', padx=15,
                     pady=5, width=3, command=lambda: click(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=cerceve, text='2', padx=15,
                     pady=5, width=3, command=lambda: click(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=cerceve, text='3', padx=15,
                     pady=5, width=3, command=lambda: click(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=cerceve, text='4', padx=15,
                     pady=5, width=3, command=lambda: click(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=cerceve, text='5', padx=15,
                     pady=5, width=3, command=lambda: click(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=cerceve, text='6', padx=15,
                     pady=5, width=3, command=lambda: click(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=cerceve, text='7', padx=15,
                     pady=5, width=3, command=lambda: click(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=cerceve, text='8', padx=15,
                     pady=5, width=3, command=lambda: click(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=cerceve, text='9', padx=15,
                     pady=5, width=3, command=lambda: click(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=cerceve, text='0', padx=15,
                     pady=5, width=3, command=lambda: click(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=cerceve, text="+", padx=15,
                       pady=5, width=3, command=lambda: click('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(
    master=cerceve, text="-", padx=15, pady=5, width=3, command=lambda: click('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(
    master=cerceve, text="*", padx=15, pady=5, width=3, command=lambda: click('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=cerceve, text="/", padx=15,
                       pady=5, width=3, command=lambda: click('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=cerceve, text="clear",
                         padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=cerceve, text="=", padx=15,
                         pady=5, width=9, command=esit)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

pencere.mainloop()
