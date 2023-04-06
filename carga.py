import xml.etree.ElementTree as ET
import os
from clasesDatos import *
from nodo import *


# ----------- LISTA APARTADO DE MAQUINAS -----------#
lista_ElementosGeneral = ListaSimple()
def get_listaElementosGeneral():
    return lista_ElementosGeneral
#---------------------------------------------------#


# ----------- LISTA APARTADO DE MAQUINAS -----------#
lista_ElementosPin = listaDoble()
def get_listaElementosNodo():
    return lista_ElementosPin

lista_PinesMaquina = ListaSimple()
def get_PinesMaquina():
    return lista_PinesMaquina

lista_Maquinas = ListaSimple()
def get_listaMaquinas():
    return lista_Maquinas
#---------------------------------------------------#


# ----------- LISTA APARTADO DE COMPUESTOS  -----------#
lista_ElementosCompuesto = ListaSimple()
def get_ElementosCompuesto():
    return lista_ElementosCompuesto

lista_Compuestos = ListaSimple()
def get_Compuestos():
    return lista_Compuestos
#---------------------------------------------------#

rutaInfo = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\entrada_proyecto2_dummy.xml"


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    
    contador = 0
    ListaPinError = []
    for Maquina in root.findall(".//listaMaquinas/Maquina"):

        # Comprobacion numero de Pines
        numeroPines = Maquina.find("numeroPines").text
        listaPines  = Maquina.findall("pin")
        numeroPines = int(numeroPines)


        # Comprobacion Numero de Elementos
        cantidadElementos = Maquina.find("numeroElementos").text
        listaElementos = Maquina.findall("pin/elementos/elemento")
        cantidadElementos = int(cantidadElementos)
        
        contador += 1

        #print(len(listaPines), numeroPines)
    
        elementosPines = (cantidadElementos / (len(listaPines)))
        #numeroCompuestoprint(elementosPines)

        if (len(listaPines) != numeroPines):
            ListaPinError.append(contador)

        #print(len(listaElementos), (cantidadElementos*numeroPines))

    #print(ListaElemetosError)



    if (len(ListaPinError) != 0):
        print("Existe Error con los PINES del XML en las Siguientes Maquinas: ")
        for x in ListaPinError:
            print(f"Maquina: {x}")

    elif (len(listaElementos) != cantidadElementos): 
        print("Existe Error con los ELEMENTOS del XML en las Maquinas: ")


    else:
        # --------------- LECTURA LISTA DE ELEMENTOS ------------------ #
        lista_ElementosGeneral.limpiar()
        contadorElemento =0
        for elemento in root.findall(".//listaElementos/elemento"):
            numeroAtomico = elemento.find("numeroAtomico").text
            simbolo = elemento.find("simbolo").text
            nombreElemento = elemento.find("nombreElemento").text
            contadorElemento += 1
            
            listaData_temp = dataElementosGeneral(contadorElemento, numeroAtomico, simbolo, nombreElemento)
            lista_ElementosGeneral._agregar_final(listaData_temp)
            
        lista_ElementosGeneral.bubble_sort()
 
        

        # --------------- LECTURA LISTA DE MAQUINAS ------------------ #
        contadorMaquina = 0
        for Maquina in root.findall(".//listaMaquinas/Maquina"):
            nombre = Maquina.find("nombre").text
            numeroPines = Maquina.find("numeroPines").text
            numeroElementos = Maquina.find("numeroElementos").text
            contadorMaquina += 1
            contadorPin = 0
        
            #print(f"Nombre: {nombre}, Numero Pines: {numeroPines}, Numero Elementos: {numeroElementos}")
            
            lista_PinesMaquina = ListaSimple()

            # Recorre cada pin de la maquina
            for pines in Maquina.findall("pin"):

                # Resetea la lista donde se guardaran los elementos de cada pin
                lista_ElementosPin = listaDoble()
                contadorPin += 1
                contadorElemento = 0
                
                # Recorre cada uno de los elementos del pin
                for elementos in pines.findall("elementos/elemento"):
                    elemento = elementos.text
                    contadorElemento += 1

                    # Carga de datos en la lista de elementos 
                    listaData_temp = dataElementoPin(elemento, contadorElemento)
                    lista_ElementosPin._agregar_final(listaData_temp)
                                  
                
                # Carga de datos en la lista te pines
                listaData_temp = dataPin(lista_ElementosPin, contadorPin)
                lista_PinesMaquina._agregar_final(listaData_temp)
            
            # Carga de datos en la lista de maquina. lista superior
            listaData_temp = dataMaquina(nombre, numeroPines, numeroElementos, contadorMaquina, lista_PinesMaquina)
            lista_Maquinas._agregar_final(listaData_temp)


        
        # --------------- LECTURA LISTA DE COMPUESTOS ------------------ #
        contadorCompuesto = 0
        for compuesto in root.findall(".//listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text
            contadorCompuesto += 1
            contador = 0

            lista_ElementosCompuesto = ListaSimple()
            for elementos in compuesto.findall("elementos/elemento"):
                elemento = elementos.text
                contador += 1
                
                listaData_temp = dataCompuestoElemento(elemento, contador)
                lista_ElementosCompuesto._agregar_final(listaData_temp)

            listaElementos_temp = dataCompuesto(nombre, contadorCompuesto, lista_ElementosCompuesto)
            lista_Compuestos._agregar_final(listaElementos_temp)


                # #print(f"Nombre: {nombre}, Elemento: {elemento}")
                # (len(compuesto.findall("elementos/elemento")))
                

# print("\n\n\n")

#---------- RECORRRIDO LISTA ELEMENTOS GENERAL ------------#
# nodo_actual = lista_ElementosGeneral.primero
# while nodo_actual != None:
#     print(f"No. {nodo_actual.dato.contador} --> No. Atomic: {nodo_actual.dato.numeroAtomico} --> Simbolo: {nodo_actual.dato.simbolo} --> Nombre: {nodo_actual.dato.nombreElemento}")
#     nodo_actual = nodo_actual.siguiente


#---------- RECORRRIDO LISTA MAQUINAS ------------#
# nodo_primeroMaquinas = lista_Maquinas.primero
# while nodo_primeroMaquinas != None:
#     nodo_pines = nodo_primeroMaquinas.dato.listaPines.primero
#     while(nodo_pines != None):
#         nodo_elementos = nodo_pines.dato.listaPin.primero
#         while(nodo_elementos != None):
#             print(f"Maquina: {nodo_primeroMaquinas.dato.numeroDeMaquina} --> Pin: {nodo_pines.dato.contadorPin} --> Elemento: {nodo_elementos.dato.elementoPin}")
            
#             nodo_elementos = nodo_elementos.siguiente
#         nodo_pines = nodo_pines.siguiente
#     nodo_primeroMaquinas = nodo_primeroMaquinas.siguiente


#---------- RECORRRIDO LISTA COMPUESTOS ------------#
# nodo_actualCompuestos = lista_Compuestos.primero
# while nodo_actualCompuestos != None:
#     nodo_actualElementos = nodo_actualCompuestos.dato.listaCompuestos.primero
#     while nodo_actualElementos != None:
#         print(f"Compuesto: {nodo_actualCompuestos.dato.nombreCompuesto, nodo_actualCompuestos.dato.numeroCompuesto} --> Elemento: {nodo_actualElementos.dato.elemento} --> No.: {nodo_actualElementos.dato.numeroElemento}")
#         nodo_actualElementos = nodo_actualElementos.siguiente
#     nodo_actualCompuestos = nodo_actualCompuestos.siguiente


