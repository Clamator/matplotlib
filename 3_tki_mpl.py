import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, MultipleLocator, MaxNLocator

win = tk.Tk()
win.geometry('600x400+300+200')

def graph_pole():
    #fig = plt.figure(figsize=(5, 5))
    #ax = fig.add_subplot()
    #lines1 = ax.plot([1, 5, 1, 5], [1, 5, 5, 1])
    #plt.show()
    win2 = tk.Toplevel()
    win2.title('Graph')
    win2.geometry('600x400+300+200')

    def show_graph():
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot()
        lines1 = ax.plot([1, 5, 1, 5], [1, 5, 5, 1])
        plt.show()

    button1 = tk.Button(win2, text='graph1', command=show_graph).grid()
    button2 = tk.Button(win2, text='graph1', command=show_graph).grid()



button = tk.Button(text='Graph', command=graph_pole)
button.pack()
win.mainloop()
