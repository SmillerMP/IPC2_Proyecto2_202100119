
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

from carga import get_listaElementosGeneral
from carga import *
from funcionesGui import *


listaGeneralElementos = get_listaElementosGeneral()
listaMaquinas = get_listaMaquinas()
listaCompuestos = get_Compuestos()


# FUNCIONES PARA EL MANEJO DE LOS BOTONES 
#-------------------------------------------#
def abrir_archivo_xml():
    abrir_Archivo()

def documentacion():
    rutaDoc = "Documentacion"
    os.startfile(rutaDoc)
#-------------------------------------------#



# ventana para la lista de elementos
def abrir_listado_elementos():
    
    listado_elementos = tk.Toplevel(ventana_principal)
    listado_elementos.geometry("406x381+601+217")
    listado_elementos.minsize(120, 1)
    listado_elementos.maxsize(3290, 1061)
    listado_elementos.resizable(1,  1)
    listado_elementos.title("Listado de Elementos")
    listado_elementos.configure(background="#E7DFD5")
    listado_elementos.configure(highlightbackground="#d9d9d9")
    listado_elementos.configure(highlightcolor="black")
 

    Label1_1 = tk.Label(listado_elementos)
    Label1_1.configure(activebackground="#f9f9f9")
    Label1_1.configure(background="#204051")
    Label1_1.configure(borderwidth="0")
    Label1_1.configure(compound='left')
    Label1_1.configure(disabledforeground="#a3a3a3")
    Label1_1.configure(font="-family {Consolas} -size 14 -weight bold")
    Label1_1.configure(foreground="#E7DFD5")
    Label1_1.configure(highlightbackground="#d9d9d9")
    Label1_1.configure(highlightcolor="black")
    Label1_1.configure(text='''Listado de Elementos''')
    

    # Tabla de elementos
    tabla = ttk.Treeview(listado_elementos)
    # Agregar columnas a la tabla

    # Configuracion de la scrollbar
    scrollbar = tk.Scrollbar(listado_elementos, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    tabla['columns'] = ('Numero Atomico', 'Elemento', 'Simbolo')

    # Formatear columnas
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('Numero Atomico', anchor=tk.CENTER, width=80)
    tabla.column('Elemento', anchor=tk.CENTER, width=120)
    tabla.column('Simbolo', anchor=tk.CENTER, width=70)

    # Agregar encabezados de columna
    tabla.heading('#0', text='', anchor=tk.CENTER)
    tabla.heading('Numero Atomico', text='Numero Atomico', anchor=tk.CENTER)
    tabla.heading('Elemento', text='Elemento', anchor=tk.CENTER)
    tabla.heading('Simbolo', text='Simbolo', anchor=tk.CENTER)

    listaGeneralElementos.bubble_sort()

    contador = 0
    nodo_actual = listaGeneralElementos.primero
    while nodo_actual != None:
        #print(f"No. {nodo_actual.dato.contador} --> No. Atomic: {nodo_actual.dato.numeroAtomico} --> Simbolo: {nodo_actual.dato.simbolo} --> Nombre: {nodo_actual.dato.nombreElemento}")
        tabla.insert(parent='', index=contador, iid=contador, text='', values=(nodo_actual.dato.numeroAtomico, nodo_actual.dato.nombreElemento, nodo_actual.dato.simbolo))
        contador += 1
        nodo_actual = nodo_actual.siguiente


    Label1_1.place(relx=0.0, rely=0.0, height=43, width=412)
    tabla.place(relx=0.0, rely=0.11, relheight=0.9, relwidth=0.95)
    scrollbar.place(relx=0.95, rely=0.11, relheight=0.9, relwidth=0.05)
    ventana_principal.resizable(0, 0)


# NUEVOS ELEMENTOS
# Ventana para nuevos elementos
def abrir_agregar_elementos():
    
    def agregar():
        agregar_elemento(Incertar_nombreElemento, Incertar_simboloElemento, incertar_numeroAtomico, agregar_elementos)

    agregar_elementos = tk.Toplevel(ventana_principal)

    agregar_elementos.geometry("439x302+601+217")
    agregar_elementos.minsize(120, 1)
    agregar_elementos.maxsize(3290, 1061)
    agregar_elementos.resizable(1,  1)
    agregar_elementos.title("Agregar Elemento")
    agregar_elementos.configure(background="#E7DFD5")
    agregar_elementos.configure(highlightbackground="#d9d9d9")
    agregar_elementos.configure(highlightcolor="black")


    Label1_1_1 = tk.Label(agregar_elementos)
    Label1_1_1.place(relx=0.0, rely=0.0, height=39, width=442)
    Label1_1_1.configure(activebackground="#f9f9f9")
    Label1_1_1.configure(background="#204051")
    Label1_1_1.configure(borderwidth="0")
    Label1_1_1.configure(compound='left')
    Label1_1_1.configure(disabledforeground="#a3a3a3")
    Label1_1_1.configure(font="-family {Consolas} -size 14 -weight bold")
    Label1_1_1.configure(foreground="#E7DFD5")
    Label1_1_1.configure(highlightbackground="#d9d9d9")
    Label1_1_1.configure(highlightcolor="black")
    Label1_1_1.configure(text='''Agregar Elementos''')
    
    
    Incertar_nombreElemento = tk.Entry(agregar_elementos)
    Incertar_nombreElemento.place(relx=0.456, rely=0.265, height=30
            , relwidth=0.419)
    
    Incertar_nombreElemento.configure(background="white")
    Incertar_nombreElemento.configure(disabledforeground="#a3a3a3")
    Incertar_nombreElemento.configure(font="-family {Arial} -size 10 -weight bold")
    Incertar_nombreElemento.configure(foreground="#000000")
    Incertar_nombreElemento.configure(highlightbackground="#d9d9d9")
    Incertar_nombreElemento.configure(highlightcolor="black")
    Incertar_nombreElemento.configure(insertbackground="black")
    Incertar_nombreElemento.configure(selectbackground="#c4c4c4")
    Incertar_nombreElemento.configure(selectforeground="black")

    Label4 = tk.Label(agregar_elementos)
    Label4.place(relx=0.068, rely=0.265, height=31, width=155)
    Label4.configure(activebackground="#f9f9f9")
    Label4.configure(background="#3B6978")
    Label4.configure(compound='left')
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Arial} -size 10 -weight bold")
    Label4.configure(foreground="#000000")
    Label4.configure(highlightbackground="#d9d9d9")
    Label4.configure(highlightcolor="black")
    Label4.configure(text='''Nombre del Elemento''')

    Label4_1 = tk.Label(agregar_elementos)
    Label4_1.place(relx=0.068, rely=0.596, height=31, width=155)
    Label4_1.configure(activebackground="#f9f9f9")
    Label4_1.configure(background="#3B6978")
    Label4_1.configure(compound='left')
    Label4_1.configure(disabledforeground="#a3a3a3")
    Label4_1.configure(font="-family {Arial} -size 10 -weight bold")
    Label4_1.configure(foreground="#000000")
    Label4_1.configure(highlightbackground="#d9d9d9")
    Label4_1.configure(highlightcolor="black")
    Label4_1.configure(text='''Numero Atomico''')

    Label4_1_1 = tk.Label(agregar_elementos)
    Label4_1_1.place(relx=0.068, rely=0.43, height=31, width=155)
    Label4_1_1.configure(activebackground="#f9f9f9")
    Label4_1_1.configure(background="#3B6978")
    Label4_1_1.configure(compound='left')
    Label4_1_1.configure(disabledforeground="#a3a3a3")
    Label4_1_1.configure(font="-family {Arial} -size 10 -weight bold")
    Label4_1_1.configure(foreground="#000000")
    Label4_1_1.configure(highlightbackground="#d9d9d9")
    Label4_1_1.configure(highlightcolor="black")
    Label4_1_1.configure(text='''Simbolo del Elemento''')

    Incertar_simboloElemento = tk.Entry(agregar_elementos)
    Incertar_simboloElemento.place(relx=0.456, rely=0.43, height=30
            , relwidth=0.419)
    
    Incertar_simboloElemento.configure(background="white")
    Incertar_simboloElemento.configure(disabledforeground="#a3a3a3")
    Incertar_simboloElemento.configure(font="-family {Arial} -size 10 -weight bold")
    Incertar_simboloElemento.configure(foreground="#000000")
    Incertar_simboloElemento.configure(highlightbackground="#d9d9d9")
    Incertar_simboloElemento.configure(highlightcolor="black")
    Incertar_simboloElemento.configure(insertbackground="black")
    Incertar_simboloElemento.configure(selectbackground="#c4c4c4")
    Incertar_simboloElemento.configure(selectforeground="black")
    incertar_numeroAtomico = tk.Entry(agregar_elementos)
    incertar_numeroAtomico.place(relx=0.456, rely=0.596, height=30
            , relwidth=0.419)

    incertar_numeroAtomico.configure(background="white")
    incertar_numeroAtomico.configure(disabledforeground="#a3a3a3")
    incertar_numeroAtomico.configure(font="-family {Arial} -size 10 -weight bold")
    incertar_numeroAtomico.configure(foreground="#000000")
    incertar_numeroAtomico.configure(highlightbackground="#d9d9d9")
    incertar_numeroAtomico.configure(highlightcolor="black")
    incertar_numeroAtomico.configure(insertbackground="black")
    incertar_numeroAtomico.configure(selectbackground="#c4c4c4")
    incertar_numeroAtomico.configure(selectforeground="black")
    incertar_botonCargar = tk.Button(agregar_elementos)
    incertar_botonCargar.place(relx=0.319, rely=0.795, height=34
            , width=147)
    
    incertar_botonCargar.configure(activebackground="beige")
    incertar_botonCargar.configure(activeforeground="black")
    incertar_botonCargar.configure(background="#FF8787")
    incertar_botonCargar.configure(compound='left')
    incertar_botonCargar.configure(disabledforeground="#a3a3a3")
    incertar_botonCargar.configure(foreground="#000000")
    incertar_botonCargar.configure(highlightbackground="#d9d9d9")
    incertar_botonCargar.configure(highlightcolor="black")
    incertar_botonCargar.configure(pady="0")
    incertar_botonCargar.configure(text='''Agregar Elemento''')
    incertar_botonCargar.configure(command=agregar)


    agregar_elementos.resizable(0,0)


# Ventana para la experimentacion
def experimento():

    def botonCorrer():
        expermiento_funcion(nombre_maquina, nombre_compuesto, ventana_experimento)

    def botonMaquinas():
        reporte_maquinas(ventana_experimento)

    ventana_experimento = tk.Toplevel(ventana_principal)
    ventana_experimento.geometry("805x492+581+342")
    ventana_experimento.minsize(120, 1)
    ventana_experimento.maxsize(3290, 1061)
    ventana_experimento.resizable(1,  1)
    ventana_experimento.title("Experimento")
    ventana_experimento.configure(background="#E7DFD5")


    Label1_2 = tk.Label(ventana_experimento)
    Label1_2.place(relx=-0.02, rely=0.0, height=42, width=823)
    Label1_2.configure(activebackground="#f9f9f9")
    Label1_2.configure(background="#204051")
    Label1_2.configure(borderwidth="0")
    Label1_2.configure(compound='left')
    Label1_2.configure(disabledforeground="#a3a3a3")
    Label1_2.configure(font="-family {Consolas} -size 14 -weight bold")
    Label1_2.configure(foreground="#E7DFD5")
    Label1_2.configure(highlightbackground="#d9d9d9")
    Label1_2.configure(highlightcolor="black")
    Label1_2.configure(text='''Experimento''')

    Label1_2_1 = tk.Label(ventana_experimento)
    Label1_2_1.place(relx=0.422, rely=0.142, height=23, width=465)
    Label1_2_1.configure(activebackground="#f9f9f9")
    Label1_2_1.configure(background="#84A9AC")
    Label1_2_1.configure(borderwidth="0")
    Label1_2_1.configure(compound='left')
    Label1_2_1.configure(disabledforeground="#a3a3a3")
    Label1_2_1.configure(font="-family {Consolas} -size 12 -weight bold")
    Label1_2_1.configure(foreground="#000000")
    Label1_2_1.configure(highlightbackground="#d9d9d9")
    Label1_2_1.configure(highlightcolor="black")
    Label1_2_1.configure(text='''Lista de Maquinas''')
    Label1_2_1_1 = tk.Label(ventana_experimento)
    Label1_2_1_1.place(relx=0.422, rely=0.569, height=22, width=465)
    Label1_2_1_1.configure(activebackground="#f9f9f9")
    Label1_2_1_1.configure(background="#84A9AC")
    Label1_2_1_1.configure(borderwidth="0")
    Label1_2_1_1.configure(compound='left')
    Label1_2_1_1.configure(disabledforeground="#a3a3a3")
    Label1_2_1_1.configure(font="-family {Consolas} -size 12 -weight bold")
    Label1_2_1_1.configure(foreground="#000000")
    Label1_2_1_1.configure(highlightbackground="#d9d9d9")
    Label1_2_1_1.configure(highlightcolor="black")
    Label1_2_1_1.configure(text='''Lista de Compuestos''')

    TSeparator2 = ttk.Separator(ventana_experimento)
    TSeparator2.place(relx=0.422, rely=0.142,  relheight=0.854)
    TSeparator2.configure(orient="vertical")

    boton_correr_experimento = tk.Button(ventana_experimento)
    boton_correr_experimento.place(relx=0.099, rely=0.65, height=34
        , width=187)
    boton_correr_experimento.configure(activebackground="beige")
    boton_correr_experimento.configure(activeforeground="black")
    boton_correr_experimento.configure(background="#FF8787")
    boton_correr_experimento.configure(compound='left')
    boton_correr_experimento.configure(disabledforeground="#a3a3a3")
    boton_correr_experimento.configure(foreground="#000000")
    boton_correr_experimento.configure(highlightbackground="#d9d9d9")
    boton_correr_experimento.configure(highlightcolor="black")
    boton_correr_experimento.configure(pady="0")
    boton_correr_experimento.configure(text='''Correr Experimento''')
    boton_correr_experimento.configure(command=botonCorrer)

    Label1_2_1_2 = tk.Label(ventana_experimento)
    Label1_2_1_2.place(relx=0.0, rely=0.142, height=23, width=348)
    Label1_2_1_2.configure(activebackground="#f9f9f9")
    Label1_2_1_2.configure(background="#84A9AC")
    Label1_2_1_2.configure(borderwidth="0")
    Label1_2_1_2.configure(compound='left')
    Label1_2_1_2.configure(disabledforeground="#a3a3a3")
    Label1_2_1_2.configure(font="-family {Consolas} -size 12 -weight bold")
    Label1_2_1_2.configure(foreground="#000000")
    Label1_2_1_2.configure(highlightbackground="#d9d9d9")
    Label1_2_1_2.configure(highlightcolor="black")
    Label1_2_1_2.configure(text='''Datos para Experimento''')

    Label1_2_1_2_1 = tk.Label(ventana_experimento)
    Label1_2_1_2_1.place(relx=0.0, rely=0.264, height=23, width=337)
    Label1_2_1_2_1.configure(activebackground="#f9f9f9")
    Label1_2_1_2_1.configure(background="#E7DFD5")
    Label1_2_1_2_1.configure(borderwidth="0")
    Label1_2_1_2_1.configure(compound='left')
    Label1_2_1_2_1.configure(disabledforeground="#a3a3a3")
    Label1_2_1_2_1.configure(font="-family {Consolas} -size 12 -weight bold")
    Label1_2_1_2_1.configure(foreground="#000000")
    Label1_2_1_2_1.configure(highlightbackground="#d9d9d9")
    Label1_2_1_2_1.configure(highlightcolor="black")
    Label1_2_1_2_1.configure(text='''Escriba el nombre de la Maquina''')

    nombre_maquina = tk.Entry(ventana_experimento)
    nombre_maquina.place(relx=0.099, rely=0.325, height=30
        , relwidth=0.229)
    nombre_maquina.configure(background="white")
    nombre_maquina.configure(disabledforeground="#a3a3a3")
    nombre_maquina.configure(font="-family {Arial} -size 10 -weight bold")
    nombre_maquina.configure(foreground="#000000")
    nombre_maquina.configure(highlightbackground="#d9d9d9")
    nombre_maquina.configure(highlightcolor="black")
    nombre_maquina.configure(insertbackground="black")
    nombre_maquina.configure(selectbackground="#c4c4c4")
    nombre_maquina.configure(selectforeground="black")

    Label1_2_1_2_1_1 = tk.Label(ventana_experimento)
    Label1_2_1_2_1_1.place(relx=0.0, rely=0.467, height=23, width=338)
    Label1_2_1_2_1_1.configure(activebackground="#f9f9f9")
    Label1_2_1_2_1_1.configure(background="#E7DFD5")
    Label1_2_1_2_1_1.configure(borderwidth="0")
    Label1_2_1_2_1_1.configure(compound='left')
    Label1_2_1_2_1_1.configure(disabledforeground="#a3a3a3")
    Label1_2_1_2_1_1.configure(font="-family {Consolas} -size 12 -weight bold")
    Label1_2_1_2_1_1.configure(foreground="#000000")
    Label1_2_1_2_1_1.configure(highlightbackground="#d9d9d9")
    Label1_2_1_2_1_1.configure(highlightcolor="black")
    Label1_2_1_2_1_1.configure(text='''Escriba el nombre del Compuesto''')

    nombre_compuesto = tk.Entry(ventana_experimento)
    nombre_compuesto.place(relx=0.099, rely=0.528, height=30
        , relwidth=0.229)
    nombre_compuesto.configure(background="white")
    nombre_compuesto.configure(disabledforeground="#a3a3a3")
    nombre_compuesto.configure(font="-family {Arial} -size 10 -weight bold")
    nombre_compuesto.configure(foreground="#000000")
    nombre_compuesto.configure(highlightbackground="#d9d9d9")
    nombre_compuesto.configure(highlightcolor="black")
    nombre_compuesto.configure(insertbackground="black")
    nombre_compuesto.configure(selectbackground="#c4c4c4")
    nombre_compuesto.configure(selectforeground="black")

    tabla_maquinas = ttk.Treeview(ventana_experimento)
    # Agregar columnas a la tabla

    # Configuracion de la scrollbar
    scrollbar = tk.Scrollbar(ventana_experimento, orient="vertical", command=tabla_maquinas.yview)
    tabla_maquinas.configure(yscrollcommand=scrollbar.set)

    tabla_maquinas['columns'] = ('Maquina', 'Nombre', 'No. Pines', 'No. Elementos')

    # Formatear columnas
    tabla_maquinas.column('#0', width=0, stretch=tk.NO)
    tabla_maquinas.column('Maquina', anchor=tk.CENTER, width=70)
    tabla_maquinas.column('Nombre', anchor=tk.CENTER, width=120)
    tabla_maquinas.column('No. Pines', anchor=tk.CENTER, width=70)
    tabla_maquinas.column('No. Elementos', anchor=tk.CENTER, width=75)

    # Agregar encabezados de columna
    tabla_maquinas.heading('#0', text='', anchor=tk.CENTER)
    tabla_maquinas.heading('Maquina', text='Maquina', anchor=tk.CENTER)
    tabla_maquinas.heading('Nombre', text='Nombre', anchor=tk.CENTER)
    tabla_maquinas.heading('No. Pines', text='No. Pines', anchor=tk.CENTER)
    tabla_maquinas.heading('No. Elementos', text='No. Elementos', anchor=tk.CENTER)


    contador = 1
    nodo_actual = listaMaquinas.primero
    while nodo_actual != None:
        tabla_maquinas.insert(parent='', index=contador, iid=contador, text='', values=(contador, nodo_actual.dato.nombreMaquina, nodo_actual.dato.numeroDePines, nodo_actual.dato.numeroDeElementos))
        contador += 1
        nodo_actual = nodo_actual.siguiente


    tabla_maquinas.place(relx=0.424, rely=0.19, relheight=0.35, relwidth=0.546)
    scrollbar.place(relx=0.97, rely=0.19, relheight=0.35, relwidth=0.03)




    tabla_compuestos = ttk.Treeview(ventana_experimento)
    # Agregar columnas a la tabla

    # Configuracion de la scrollbar
    scrollbarCompuestos = tk.Scrollbar(ventana_experimento, orient="vertical", command=tabla_compuestos.yview)
    tabla_compuestos.configure(yscrollcommand=scrollbar.set)

    tabla_compuestos['columns'] = ('No. Compuesto', 'Compuesto', 'Elementos')

    # Formatear columnas
    tabla_compuestos.column('#0', width=0, stretch=tk.NO)
    tabla_compuestos.column('No. Compuesto', anchor=tk.CENTER, width=30)
    tabla_compuestos.column('Compuesto', anchor=tk.CENTER, width=30)
    tabla_compuestos.column('Elementos', anchor=tk.CENTER, width=140)

    # Agregar encabezados de columna
    tabla_compuestos.heading('#0', text='', anchor=tk.CENTER)
    tabla_compuestos.heading('No. Compuesto', text='No. Compuesto', anchor=tk.CENTER)
    tabla_compuestos.heading('Compuesto', text='Compuesto', anchor=tk.CENTER)
    tabla_compuestos.heading('Elementos', text='Elementos', anchor=tk.CENTER)

    contador = 1
    elementos = ""
    nodo_actual = listaCompuestos.primero
    while nodo_actual != None:
        nodo_especifico = nodo_actual.dato.listaCompuestos.primero
        while nodo_especifico != None:
            elementos += nodo_especifico.dato.elemento
            elementos += ", "
            nodo_especifico = nodo_especifico.siguiente

        tabla_compuestos.insert(parent='', index=contador, iid=contador, text='', values=(contador, nodo_actual.dato.nombreCompuesto, elementos))
        contador += 1
        elementos = ""
        nodo_actual = nodo_actual.siguiente

    tabla_compuestos.place(relx=0.424, rely=0.614, relheight=0.35, relwidth=0.546)
    scrollbarCompuestos.place(relx=0.97, rely=0.614, relheight=0.35, relwidth=0.03)



    boton_maquinas = tk.Button(ventana_experimento)
    boton_maquinas.place(relx=0.099, rely=0.9, height=34
        , width=187)
    boton_maquinas.configure(activebackground="beige")
    boton_maquinas.configure(activeforeground="black")
    boton_maquinas.configure(background="#84A9AC")
    boton_maquinas.configure(compound='left')
    boton_maquinas.configure(disabledforeground="#a3a3a3")
    boton_maquinas.configure(foreground="#000000")
    boton_maquinas.configure(highlightbackground="#d9d9d9")
    boton_maquinas.configure(highlightcolor="black")
    boton_maquinas.configure(pady="0")
    boton_maquinas.configure(text='''Reporte de Maquinas''')
    boton_maquinas.configure(command=botonMaquinas)


    ventana_experimento.resizable(0, 0)
    



# Pagina Principal


ventana_principal = tk.Tk()
ventana_principal.geometry("712x417+601+217")
ventana_principal.minsize(120, 1)
ventana_principal.maxsize(3290, 1061)
ventana_principal.resizable(1,  1)
ventana_principal.title("Menu Principal")
ventana_principal.configure(background="#E7DFD5")
ventana_principal.configure(highlightbackground="#d9d9d9")
ventana_principal.configure(highlightcolor="black")



Label1 = tk.Label(ventana_principal)
Label1.place(relx=0.0, rely=0.0, height=47, width=717)
Label1.configure(activebackground="#f9f9f9")
Label1.configure(background="#204051")
Label1.configure(borderwidth="0")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font="-family {Consolas} -size 14 -weight bold")
Label1.configure(foreground="#E7DFD5")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text='''Proyecto 2 IPC 2''')



Button1 = tk.Button(ventana_principal)
Button1.place(relx=0.042, rely=0.333, height=44, width=177)
Button1.configure(activebackground="beige")
Button1.configure(activeforeground="black")
Button1.configure(background="#84A9AC")
Button1.configure(compound='left')
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font="-family {Arial} -size 10 -weight bold")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Listado de Elementos''')
Button1.configure(command=abrir_listado_elementos)

Label2 = tk.Label(ventana_principal)
Label2.place(relx=0.14, rely=0.199, height=38, width=220)
Label2.configure(activebackground="#f9f9f9")
Label2.configure(background="#3B6978")
Label2.configure(compound='left')
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font="-family {Arial} -size 11 -weight bold")
Label2.configure(foreground="#000000")
Label2.configure(highlightbackground="#d9d9d9")
Label2.configure(highlightcolor="black")
Label2.configure(text='''Elementos Quimicos''')
Button2 = tk.Button(ventana_principal)

Button2.place(relx=0.309, rely=0.333, height=44, width=177)
Button2.configure(activebackground="beige")
Button2.configure(activeforeground="black")
Button2.configure(background="#84A9AC")
Button2.configure(compound='left')
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font="-family {Arial} -size 10 -weight bold")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Agregar Elemento''')
Button2.configure(command=abrir_agregar_elementos)

Label3 = tk.Label(ventana_principal)
Label3.place(relx=0.702, rely=0.199, height=38, width=172)
Label3.configure(activebackground="#f9f9f9")
Label3.configure(background="#3B6978")
Label3.configure(compound='left')
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(font="-family {Arial} -size 11 -weight bold")
Label3.configure(foreground="#000000")
Label3.configure(highlightbackground="#d9d9d9")
Label3.configure(highlightcolor="black")
Label3.configure(text='''Manejo de XML''')

Button3 = tk.Button(ventana_principal)
Button3.place(relx=0.702, rely=0.333, height=44, width=177)
Button3.configure(activebackground="beige")
Button3.configure(activeforeground="black")
Button3.configure(background="#84A9AC")
Button3.configure(compound='left')
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font="-family {Arial} -size 10 -weight bold")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''Cargar Archivo XML''')
Button3.configure(command=abrir_archivo_xml)

Label2_1 = tk.Label(ventana_principal)
Label2_1.place(relx=0.379, rely=0.624, height=38, width=172)
Label2_1.configure(activebackground="#f9f9f9")
Label2_1.configure(background="#3B6978")
Label2_1.configure(compound='left')
Label2_1.configure(disabledforeground="#a3a3a3")
Label2_1.configure(font="-family {Arial} -size 11 -weight bold")
Label2_1.configure(foreground="#000000")
Label2_1.configure(highlightbackground="#d9d9d9")
Label2_1.configure(highlightcolor="black")
Label2_1.configure(text='''Experimento''')

BotonExperimento = tk.Button(ventana_principal)
BotonExperimento.place(relx=0.379, rely=0.743, height=44, width=177)
BotonExperimento.configure(activebackground="beige")
BotonExperimento.configure(activeforeground="black")
BotonExperimento.configure(background="#84A9AC")
BotonExperimento.configure(compound='left')
BotonExperimento.configure(disabledforeground="#a3a3a3")
BotonExperimento.configure(font="-family {Arial} -size 10 -weight bold")
BotonExperimento.configure(foreground="#000000")
BotonExperimento.configure(highlightbackground="#d9d9d9")
BotonExperimento.configure(highlightcolor="black")
BotonExperimento.configure(pady="0")
BotonExperimento.configure(text='''Seleccionar''')
BotonExperimento.configure(command=experimento)


BotonAyuda = tk.Button(ventana_principal)
BotonAyuda.place(relx=0.85, rely=0.90, height=30, width=100)
BotonAyuda.configure(activebackground="beige")
BotonAyuda.configure(activeforeground="black")
BotonAyuda.configure(background="#84A9AC")
BotonAyuda.configure(compound='left')
BotonAyuda.configure(disabledforeground="#a3a3a3")
BotonAyuda.configure(font="-family {Arial} -size 10 -weight bold")
BotonAyuda.configure(foreground="#000000")
BotonAyuda.configure(highlightbackground="#d9d9d9")
BotonAyuda.configure(highlightcolor="black")
BotonAyuda.configure(pady="0")
BotonAyuda.configure(text='''Ayuda''')
BotonAyuda.configure(command=documentacion)





ventana_principal.mainloop()




