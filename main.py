from distutils.command.config import config
from math import radians
from tkinter import Button, Tk
from tkcalendar import Calendar
import funciones

tk = Tk()

tk.configure(bg='#42f5dd')

cal = Calendar(tk, selectmode = 'day', 
               year = 2020, month = 5, 
               day = 22).pack()

Button(tk,text="Obtener fecha:",bg="#fff",border=3, relief='groove',fg='blue',command=funciones.mensaje).pack(pady=5)


tk.mainloop()