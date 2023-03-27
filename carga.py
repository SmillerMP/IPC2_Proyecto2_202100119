import xml.etree.ElementTree as ET

from clasesDatos import datosElementos
from nodo import *




listaElementosNodo = listaDoble()

def get_listaElementosNodo():
    return listaElementosNodo




def cargaArchivo():
    ruta = "entrada_proyecto2_dummy.xml"
    tree = ET.parse(ruta)
    root = tree.getroot()

    
    contador = 0
    ListaElemetosError = []
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
        for elemento in root.findall(".//listaElementos/elemento"):
            numeroAtomico = elemento.find("numeroAtomico").text
            simbolo = elemento.find("simbolo").text
            nombreElemento = elemento.find("nombreElemento").text
            
            #print(f"Numero Atomico: {numeroAtomico}, Simbolo: {simbolo}, Nombre Elemento: {nombreElemento}")


        contadorMaquina = 0
        contadorIndice = 0
        contadorPin = 1
        contadorElementos = 0
        for Maquina in root.findall(".//listaMaquinas/Maquina"):
            nombre = Maquina.find("nombre").text
            numeroPines = Maquina.find("numeroPines").text
            numeroElementos = Maquina.find("numeroElementos").text

            listaElementos = Maquina.findall("pin/elementos/elemento")
            contadorMaquina += 1

            listaPines  = Maquina.findall("pin")
            
        
            #print(f"Nombre: {nombre}, Numero Pines: {numeroPines}, Numero Elementos: {numeroElementos}")
            

            for elementos in Maquina.findall("pin/elementos/elemento"):
                elemento = elementos.text
                contadorElementos += 1
                contadorIndice += 1


                listaElementos_temp = datosElementos(contadorMaquina, contadorPin, contadorIndice, elemento)
                listaElementosNodo._agregar_inicio(listaElementos_temp)

                # Indica el numero de Pin donde esta posicionado
                if contadorElementos == int(numeroElementos):
                    contadorPin += 1
                    contadorElementos = 0

                # Reincia el el Indice de elementos en la maquina
                if contadorIndice == len(listaElementos):
                    contadorIndice = 0

                # Reincia el contador de pin de la maquina
                if contadorIndice == 0:
                    contadorPin = 1

                

                
                
                #print(f"Elemento: {elemento}")
            


        for compuesto in root.findall(".//listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text


            for elementos in compuesto.findall("elementos/elemento"):
                elemento = elementos.text

                #print(f"Nombre: {nombre}, Elemento: {elemento}")

            

cargaArchivo()
listaElementosNodo._recorrer_adelante()
listaElementosNodo._size()
