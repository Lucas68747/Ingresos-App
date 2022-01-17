# Importar Bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

# Desarrollo de la Interfaz grafica

root=Tk()
root.title("Ingresos Parque Industrial")
root.geometry("610x350")
root.resizable(width=0, height=0)

miId=StringVar()
miDate=StringVar()
miHour=StringVar()
miDomain=StringVar()
miBusiness=StringVar()
miParticular=StringVar()
miDestination=StringVar()

def conexionBBDD():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE empleado (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			DATE VARCHAR(50) NOT NULL,
			HOUR VARCHAR(50) NOT NULL,
			DOMAIN VARCHAR(50) NOT NULL,
			BUSINESS VARCHAR(50) NOT NULL,
			PARTICULAR VARCHAR(50) NOT NULL,
			DESTINATION VARCHAR(50) NOT NULL)
			''')
		messagebox.showinfo("Aviso","Base de datos creada de manera exitosa")
	except:
		messagebox.showinfo("Aviso", "Conexión exitosa con la base de datos")

def eliminarBBDD():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	if messagebox.askyesno(message="Los datos serán eliminados definitivamente, ¿continuar?", title="Aviso"):
		miCursor.execute("DROP TABLE empleado")
	else:
		pass
	limpiarCampos()
	mostrar()

def salirAplicacion():
	valor=messagebox.askquestion("¿Salir?","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miDate.set("")
	miHour.set("")
	miDomain.set("")
	miBusiness.set("")
	miParticular.set("")
	miDestination.set("")

def mensaje():
	acerca='''
Tabla de ingresos
Versión 1.0
Por Lucas Emanuel Santoro
'''
	messagebox.showinfo(title="Acerca de", message=acerca)

################################ Métodos CRUD ##############################

def crear():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	try:
		datos=miDate.get(),miHour.get(),miDomain.get(),miBusiness.get(),miParticular.get(),miDestination.get()
		miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?,?,?,?)", (datos))
		miConexion.commit()
	except:
		messagebox.showwarning("Aviso","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		pass
	limpiarCampos()
	mostrar()

def mostrar():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		miCursor.execute("SELECT * FROM empleado")
		for row in miCursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
	except:
		pass

################################## Tabla ################################

tree=ttk.Treeview(height=11, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=0, y=150)
tree.column('#0', width=50)
tree.heading('#0', text="ID", anchor=CENTER)
tree.column('#1', width=80)
tree.heading('#1', text="Fecha", anchor=CENTER)
tree.column('#2', width=80)
tree.heading('#2', text="Hora", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Dominio", anchor=CENTER)
tree.column('#4', width=100)
tree.heading('#4', text="Empresa", anchor=CENTER)
tree.column('#5', width=100)
tree.heading('#5', text="Particular", anchor=CENTER)
tree.column('#6', width=100)
tree.heading('#6', text="Destino", anchor=CENTER)

def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	miDate.set(tree.item(item,"values")[0])
	miHour.set(tree.item(item,"values")[1])
	miDomain.set(tree.item(item,"values")[2])
	miBusiness.set(tree.item(item,"values")[3])
	miParticular.set(tree.item(item,"values")[4])
	miDestination.set(tree.item(item,"values")[5])

tree.bind("<Double-1>", seleccionarUsandoClick)

def actualizar():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	try:
		datos=miDate.get(), miHour.get(), miDomain.get(), miBusiness.get(), miParticular.get(), miDestination.get()
		miCursor.execute("UPDATE empleado SET DATE=?, HOUR=?, DOMAIN=?, BUSINESS=?, PARTICULAR=?, DESTINATION=? WHERE ID="+miId.get(), (datos))
		miConexion.commit()
	except:
		messagebox.showwarning("Aviso","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()
	mostrar()

def borrar():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	try:
		if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="Aviso"):
			miCursor.execute("DELETE FROM empleado WHERE ID="+miId.get())
			miConexion.commit()
	except:
		messagebox.showwarning("Aviso","Ocurrió un error al tratar de eliminar el registro")
		pass
	limpiarCampos()
	mostrar()

###################### Colocar widgets en la VISTA ######################

########## INTERFACE ELEMENTS ##########

# Menu 1

menubar=Menu(root)
menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear/Conectar base de datos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar base de datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

# Help Menu

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="Limpiar campos", command=limpiarCampos)
helpmenu.add_command(label="Acerca de", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Entry boxes

E1=Entry(root, textvariable=miDate)
L2=Label(root, text="Fecha")
L2.place(x=50,y=10)
E2=Entry(root, textvariable=miDate, width=10)
E2.place(x=100, y=10)

L3=Label(root, text="Hora")
L3.place(x=50,y=40)
E3=Entry(root, textvariable=miHour, width=10)
E3.place(x=100, y=40)

L4=Label(root, text="Dominio")
L4.place(x=40,y=70)
E4=Entry(root, textvariable=miDomain, width=10)
E4.place(x=100, y=70)

L5=Label(root, text="Empresa")
L5.place(x=200,y=10)
E5=Entry(root, textvariable=miBusiness, width=20)
E5.place(x=280, y=10)

L6=Label(root, text="Particular")
L6.place(x=200,y=40)
E6=Entry(root, textvariable=miParticular, width=20)
E6.place(x=280, y=40)

L7=Label(root, text="Destino")
L7.place(x=200,y=70)
E7=Entry(root, textvariable=miDestination, width=20)
E7.place(x=280, y=70)

# Buttons

B1=Button(root, text="Agregar entrada", command=crear)
B1.place(x=50, y=105)
B2=Button(root, text="Modificar entrada", command=actualizar)
B2.place(x=190, y=105)
B3=Button(root, text="Mostrar lista", command=mostrar)
B3.place(x=340, y=105)
B3=Button(root, text="Eliminar entrada", command=borrar)
B3.place(x=460, y=105)

root.config(menu=menubar)

root.mainloop()