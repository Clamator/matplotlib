from tkinter import*
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
flag=1

def clicked2():
    window.destroy()
    window1 = Tk()
    window1.overrideredirect(1)
    window1.state('zoomed')
    window1.title("re")
    window1.geometry('400x250')
    c = Canvas(window1, width=200,height=150,bg='blue')
    c.pack()
    x = np.linspace(-10, 10, 5000)


    print ('Введите а')
    a=float(input())
    print ('Введите b')
    b=float(input())
    print ('Введите c')
    c=float(input())
    y=a*x*x + b*x + c  

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Графики квадратичной функции: y=ax^2+bx+c", fontsize=16)
    ax.set_xlabel("x", fontsize=14)        
    ax.set_ylabel("y", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="black", linewidth=0.5)
    ax.plot(x, y, label="y = {}x^2+{}x+{}".format(a,b,c))
    ax.legend()
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)
    plt.show()
    window1.mainloop()


while flag > 0:
    window = Tk()
    window.overrideredirect(1)
    window.state('zoomed')
    window.title("re")
    c = Canvas(window, width=200,height=150,bg='blue')
    filename = PhotoImage(file = "C:\\Users\\User\\Documents\\Проект 2.0\\image2.png")
    background_label = Label(window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    c.pack()
    c.pack(side = 'left')
    btn = Button(window, text="График параболы", height=10, width=50, command=clicked2)
    canvas_widget = c.create_window(100, 100, window=btn)
    window.geometry('400x250')
    window.mainloop()