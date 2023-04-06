
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

from carga import get_listaElementosGeneral
from carga import *
from funcionesGui import *


listaGeneralElementos = get_listaElementosGeneral()

# FUNCIONES PARA EL MANEJO DE LOS BOTONES 
#-------------------------------------------#
def abrir_archivo_xml():
    abrir_Archivo()



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
    #tabla.place(relx=0.073, rely=0.157, relheight=0.331, relwidth=0.913)
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
    agregar_elementos.title("Toplevel 2")
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




# Pagina Principal

'''This class configures and populates the toplevel window.
            is the toplevel containing window.'''

ventana_principal = tk.Tk()
ventana_principal.geometry("651x450+601+217")
ventana_principal.minsize(120, 1)
ventana_principal.maxsize(3290, 1061)
ventana_principal.resizable(1,  1)
ventana_principal.title("Toplevel 0")
ventana_principal.configure(background="#E7DFD5")
ventana_principal.configure(highlightbackground="#d9d9d9")
ventana_principal.configure(highlightcolor="black")

        

Label1 = tk.Label(ventana_principal)
Label1.place(relx=0.0, rely=0.0, height=51, width=656)
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
Button1.place(relx=0.051, rely=0.333, height=44, width=177)
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
Label2.place(relx=0.051, rely=0.2, height=41, width=179)
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
Button2.place(relx=0.051, rely=0.444, height=44, width=177)
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
Label3.place(relx=0.369, rely=0.2, height=41, width=172)
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
Button3.place(relx=0.369, rely=0.333, height=44, width=177)
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

Button4 = tk.Button(ventana_principal)
Button4.place(relx=0.369, rely=0.444, height=44, width=177)
Button4.configure(activebackground="beige")
Button4.configure(activeforeground="black")
Button4.configure(background="#84A9AC")
Button4.configure(compound='left')
Button4.configure(disabledforeground="#a3a3a3")
Button4.configure(font="-family {Arial} -size 10 -weight bold")
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(text='''Generar XML''')




ventana_principal.mainloop()






