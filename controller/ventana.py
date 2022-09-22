from tkcalendar import DateEntry
from tkinter import Button, Label, StringVar, Tk
from controller import funciones


tk = Tk()
sel = StringVar()
lb = ""

def cargar_ventana():
    
    tk.configure(bg='#42f5dd')
   
    cal = DateEntry(tk, selectmode = 'day', 
               textvariable= sel).pack()
    
    #bt =Button(tk,text="Obtener fecha:",bg="#fff",border=3, relief='groove',fg='blue',command=lambda:funciones.mensaje(sel.get("33")).pack(pady=5))
    bt =Button(tk,text="Obtener fecha:",bg="#fff",border=3, relief='groove',fg='blue',command=lambda:funciones.mensaje(sel.get())).pack(pady=5)
    

    tk.mainloop()

def cambiar_label():
    lb.config(text=sel.get())
lb = Label(tk,text=sel.get(),bg='red').pack()


