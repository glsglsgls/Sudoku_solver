import tkinter as tk
from tkinter import Canvas, BOTH
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

class window:
   
    def __init__(self):
        self = tk.Tk()

    def getboard(self, arr):
        self = tk.Tk()
        for i in range(9):
            for j in range(9):
                #if (i)%3==0: padyvar = 300
                #else: padyvar=100
                #if (j)%3==0: padxvar = 300
                #else: padxvar=100
                frame = tk.Frame(
                    bg="white",
                    master=window,
                    #relief=tk.RAISED,
                    borderwidth=2
                )
                frame.grid(row=i, column=j, padx=6, pady=6)
                label = tk.Label(master=frame, text=arr[i,j], padx=5, pady=1)
                #label.place(relx=padyvar, rely=padxvar)
                label.pack()
        self.mainloop()

    def update(self,arr):
        self = tk.Tk()
        for i in range(9):
            for j in range(9):
                #if (i)%3==0: padyvar = 300
                #else: padyvar=100
                #if (j)%3==0: padxvar = 300
                #else: padxvar=100
                frame = tk.Frame(
                    bg="white",
                    master=window,
                    #relief=tk.RAISED,
                    borderwidth=2
                )
                frame.grid(row=i, column=j, padx=6, pady=6)
                label = tk.Label(master=frame, text=arr[i,j], padx=5, pady=1)
                #label.place(relx=padyvar, rely=padxvar)
                label.pack()
        self.mainloop()