# Libraries

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Interface

root=Tk()
root.title("Tabla de Ingresos")
root.geometry("600x350")

# Variables

miDate=StringVar()
miHour=StringVar()
miDomain=StringVar()
miBusiness=StringVar()
miParticular=StringVar()
miDestination=StringVar()

# Sqlite3 

def conectionDB():
    miConection=sqlite3.connect("Ingresos")
    miCursor=miConection.cursor()

# Table

    try:
        miCursor.execute('''
        CREATE TABLE datos (
            DATE VARCHAR(50) NOT NULL,
            HOUR VARCHAR(50) NOT NULL,
            DOMAIN VARCHAR(50) NOT NULL,
            BUSINESS VARCHAR(50) NOT NULL,
            PARTICULAR VARCHAR(50) NOT NULL,
            DESTINATION VARCHAR(50) NOT NULL)
        ''')
        messagebox.showinfo("CONECTION", "Base de Datos creada de manera exitosa")
    except:
        messagebox.showinfo("CONECTION", "Conexión exitosa con la base de datos")

# This function delete table

def deleteDB():
    miConection=sqlite3.connect("Ingresos")
    miCursor=miConection.cursor()
    if messagebox.askyesno(message="Los datos serán eliminados definitivamente, ¿continuar?", title="Advertencia"):
        miCursor.execute("DROP TABLE datos")
    else:
        pass    

# This is for exit

def exitApp():
    valor=messagebox.askquestion("Salir","¿Está seguro que desea salir del programa?")
    if valor=="yes":
        root.destroy()

# Clean fields

def cleanfields():
    miDate.set("")
    miHour.set("")
    miDomain.set("")
    miBusiness.set("")
    miParticular.set("")
    miDestination.set("")

# App Info

def message():
    about='''
    Tabla de Ingresos para Datos
    Versión 1.0
    By Lucas Santoro
    '''

########## CRUD METODS ##########

def create():
    miConection=sqlite3.connect("Ingresos")
    miCursor=miConection.cursor()
    try:
        data=miDate.get(),miHour.get(), miDomain.get(), miBusiness.get(), miParticular.get(), miDestination.get()
        miCursor.execute("INSERT INTO datos VALUES(?,?,?,?,?,?)", (data))
        miConection.commit()
    except:
        messagebox.showwarning("Advertencia", "Ocurrió un error al crear el registro, verifique conexión con la base de datos")
        pass
    cleanfields()
    show()

def show():
    miConection=sqlite3.connect("Ingresos")
    miCursor=miConection.cursor()
    register=tree.get_children()
    for element in register:
        tree.delete(element)
    try:
        miCursor.execute("SELECT * FROM Ingresos")
        for row in miCursor:
            tree.insert("", 0,Text=row[0], values=(row[1],row[2],row[3],row[4],row[5]))
    except:
        pass

########## TABLE ##########

tree=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text="Fecha", anchor=CENTER)
tree.column('#1', width=100)
tree.heading('#1', text="Hora", anchor=CENTER)
tree.column('#2', width=100)
tree.heading('#2', text="Dominio", anchor=CENTER)
tree.column('#3', width=110)
tree.heading('#3', text="Empresa", anchor=CENTER)
tree.column('#4', width=110)
tree.heading('#4', text="Particular", anchor=CENTER)
tree.column('#5', width=110)
tree.heading('#5', text="Destino", anchor=CENTER)

root.mainloop()
