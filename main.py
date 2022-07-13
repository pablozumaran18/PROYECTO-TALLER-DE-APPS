from cProfile import label
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import tkinter
from turtle import bgcolor
#from clases.Carrito import Carrito
#from clases.Producto import Producto
#from clases.Tienda import Tienda
#from clases.categoria import Categoria



root = Tk()
root.configure(bg = 'grey')
root.geometry ('700x500')

root.title("maquinarias jimenez")

#para escribir un texto
etiqueta = tkinter.Label(root, text="hola mundo" , bg="blue",font="arial 12") 

#para que este en el centro o en cualquier lado que uno quiera 
etiqueta.pack()

def saludo(nombre):
    print("hola" + nombre)

cajaTexto = tkinter.Entry(root, font= "helvetica 30")
cajaTexto.pack()

#con esto se usa lo que se escribe en la caja de texto y renderizarlo en la etiqueta
def textoCaja():
    texto = cajaTexto.get()
    etiqueta["text"]=texto
#------------#

boton= tkinter.Button(root,text="presionar" , command = textoCaja)

# para posicionar 

#boton.grid(row = 0,column = 1)

boton.pack()






# Variables



#def eliminar():



#def editar():



#def buscar():



# Menu de opciones
menubar = Menu(root)
root.config(menu=menubar)

createmenu = Menu(menubar, tearoff=0)

#maquinas=Menu(menubar)

menubar.add_command(label="hola mundo")
menubar.add_command(label="buscar maquina")
menubar.add_command(label="editar maquina")
menubar .add_command(label="eliminar maquina")

#menubar.add_cascade(label="OPCIONES", menu=maquinas)


#createmenu(label="Editar producto"
#createmenu(label="Lista productos"
#createmenu(label="Eliminar productos"


# FRAMES


# Frame para registro



root.mainloop()
