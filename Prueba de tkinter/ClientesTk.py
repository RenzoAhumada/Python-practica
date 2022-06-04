import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk

root = tk.Tk()
root.config(width=800, height=600)

stile=ttk.Style()
stile.configure("W.Tbutton", font =
                ('calibri', 10, 'bold','underline'),
                foreground = 'red')

label = tk.Label(text="Nombre del cliente", font = ("arial",10,"bold"))
nombre= tk.Entry(text="Nombre")
label.place(x=50,y=100)



