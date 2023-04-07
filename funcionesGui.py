import os
from pathlib import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox as MessageBox
from carga import *
from clasesDatos import *
from generadorDot import *


rutaArchivo = None
rutaGuardado = None


def abrir_Archivo():

    # Variable global para uso en otras funciones
    global rutaArchivo

    rutaArchivo = filedialog.askopenfilename(
        # Archivos compatibles
        filetypes={
            ("Archivos de texto", "*.xml"),
        }
    )

    if rutaArchivo:
        cargaArchivo(rutaArchivo)
        MessageBox.showinfo("Informacion", "Archivo XML cargado Correctamente :)")

    else:
        MessageBox.showwarning("Alerta", "No se a seleccionado ningun archivo.")



# Limpiar la caja de texto
def limpiar(cajaTexto):
    
    # Confirmacion en caso que se desee limpiar
    confirmacion = MessageBox.askyesno("Confirmar", "¿Desea Limpiar la Caja de Texto?")

    if confirmacion:
        cajaTexto.delete('1.0', tk.END)
        MessageBox.showinfo("Mensaje", "Limpieza realizada con Exito!")


# Experimento
def expermiento_funcion(textoMaquina, textoCompuesto, ventana):

    texto_maquina = textoMaquina.get()
    texto_copuesto = textoCompuesto.get()

    if generadorGrap(texto_copuesto, texto_maquina) != 404:
        textoMaquina.delete(0, tk.END)
        textoCompuesto.delete(0, tk.END)
        MessageBox.showinfo("Informacion", "Compuesto generado correctamente, Archivos correspondientes en la carpeta ../Reportes") 
        ventana.lift()
    else:
        MessageBox.showerror("Error!", "ha ocurrido unproblema, asegurese de ingresar los datos correctamente")
        ventana.lift()

# Agregar un nuevo elemento
def agregar_elemento(caja_elemento, caja_simbolo, caja_numeroAtomico, ventana):

    listaGeneralElementos = get_listaElementosGeneral()
    print(listaGeneralElementos._size())

    try:
        encontradoElemento = False
        nodo_actual = lista_ElementosGeneral.primero
        while nodo_actual != None:
            #print(f"No. {nodo_actual.dato.contador} --> No. Atomic: {nodo_actual.dato.numeroAtomico} --> Simbolo: {nodo_actual.dato.simbolo} --> Nombre: {nodo_actual.dato.nombreElemento}")
            if caja_elemento.get() == nodo_actual.dato.nombreElemento:
                encontradoElemento = True
                break
            nodo_actual = nodo_actual.siguiente

        if encontradoElemento == True:
            MessageBox.showerror("Error", "El Elemento que desea agregar ya existe en la lista")
            ventana.lift()

        encontradoSimbolo = False
        nodo_actual = lista_ElementosGeneral.primero
        while nodo_actual != None:
            if caja_simbolo.get() == nodo_actual.dato.simbolo:
                encontradoSimbolo = True
                break
            nodo_actual = nodo_actual.siguiente

        if encontradoSimbolo == True:
            MessageBox.showerror("Error", "El Simbolo que desea agregar ya existe en la lista")
            ventana.lift()


        encontradoNumeroAtomico= False
        nodo_actual = lista_ElementosGeneral.primero
        contenido = caja_numeroAtomico.get()
        while nodo_actual != None:
            #print(f"No. {nodo_actual.dato.contador} --> No. Atomic: {nodo_actual.dato.numeroAtomico} --> Simbolo: {nodo_actual.dato.simbolo} --> Nombre: {nodo_actual.dato.nombreElemento}")
            if int(contenido) == nodo_actual.dato.numeroAtomico:
                encontradoNumeroAtomico = True
                break
            nodo_actual = nodo_actual.siguiente

        if encontradoNumeroAtomico == True:
            MessageBox.showerror("Error", "El Numero Atomico que desea agregar ya existe en la lista")
            ventana.lift()
        if encontradoElemento == False and encontradoSimbolo == False and encontradoNumeroAtomico == False:
            data_temp = dataElementosGeneral(0, caja_numeroAtomico.get(), caja_simbolo.get(), caja_elemento.get())
            listaGeneralElementos._agregar_final(data_temp)
            MessageBox.showinfo("Informacion", "El elementos se ha añadido correctamente") 
            ventana.lift()

    except:
        MessageBox.showerror("Error", "Ha habido un problema con los datos que desea agegar")
        ventana.lift()