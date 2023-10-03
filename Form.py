 # -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:06:18 2023

@author: leonanardo
"""

import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)
    
def borrar():
    limpiar_campos()
    
def guardar_datos():
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    edad = entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()
    
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
        
    #Crear un cadena de datos
    datos = "Nombres:" + nombres + "\nApellidos" + apellidos + "\nEdad" + edad + "años\nEstatura" + estatura + "cm\nTelefono" + telefono + "\nGenero" + genero
    
    #Guardar los datos en un archivo de texto
    with open ("Formulario.txt", "a")as archivo:
        archivo.write(datos + "\n\n")
        
    #Mostrar un mensaje con los datos capturados
    messagebox.showinfo("informacion", "Datos guardados con exito:\n\n" + datos)
    
    #Limpiar los controles despues de guardar
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0, tk.END)
    
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")

#Crear variables para los RadioButtons
var_genero = tk.IntVar()

#Crear etiquetas y campos de entrada
label_nombres = tk.Label(ventana, text="Nombres:")
label_nombres.pack()
entry_nombres = tk.Entry(ventana)
entry_nombres.pack()

label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_estatura = tk.Label(ventana, text="Estatura:")
label_estatura.pack()
entry_estatura = tk.Entry(ventana)
entry_estatura.pack()

label_telefono = tk.Label(ventana, text="Telefono:")
label_telefono.pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

label_genero = tk.Label(ventana, text="Genero:")
label_genero.pack()

rb_hombre = tk.Radiobutton(ventana, text="Hombre",variable=var_genero,value=1)
rb_hombre.pack()

rb_mujer = tk.Radiobutton(ventana, text="Mujer",variable=var_genero,value=2)
rb_mujer.pack()

#Boton para guardar datos
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.pack()

#Boton para borrar campos
btn_borrar = tk.Button(ventana, text="Borrar Campos", command=borrar)
btn_borrar.pack()

ventana.mainloop()