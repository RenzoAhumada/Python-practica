import tkinter as tk
from tkinter import ttk



def convertir_peso():
    peso = float(boxpeso.get())

    pesodolar = peso * 124

    dolarblue = peso * 249

    labeldolar.config(text=f"Dolar: {pesodolar}")
    labeldolarblue.config(
        text=f"Dolar Blue: {dolarblue}")


window = tk.Tk()
window.title("Conversor de peso a dolar")
window.config(width=400, height=300)
labelpeso = ttk.Label(text="Cantidad en peso:")
labelpeso.place(x=20, y=20)
boxpeso = ttk.Entry()
boxpeso.place(x=140, y=20, width=60)
buttonconvert = ttk.Button(text="Convertir", command=convertir_peso)
buttonconvert.place(x=20, y=60)
labeldolar = ttk.Label(text="Precio dolar: n/a")
labeldolar.place(x=20, y=120)
labeldolarblue = ttk.Label(text="Precio dolar blue: n/a")
labeldolarblue.place(x=20, y=160)
window.mainloop() 
    