import xml.etree.ElementTree as ET

from clasesDatos import *
from nodo import *




listaElementosNodo = listaDoble()
def get_listaElementosNodo():
    return listaElementosNodo

lista_Elementos = ListaSimple()
def get_lista_Elementos():
    return lista_Elementos

lista_CompuestosElementos = ListaSimple()
def get_CompuestosElementos():
    return lista_CompuestosElementos

cola_Compuestos = colaCompuestos()
def get_cola_Compuestos():
    return cola_Compuestos


def cargaArchivo():
    ruta = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\entrada_proyecto2_dummy.xml"
    tree = ET.parse(ruta)
    root = tree.getroot()

    
    contador = 0
    elementosPines = 0
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
        for elemento in root.findall(".//listaElementos/elemento"):
            numeroAtomico = elemento.find("numeroAtomico").text
            simbolo = elemento.find("simbolo").text
            nombreElemento = elemento.find("nombreElemento").text
            
            #print(f"Numero Atomico: {numeroAtomico}, Simbolo: {simbolo}, Nombre Elemento: {nombreElemento}")


        contadorMaquina = 0
        contadorIndice = 0
        contadorPin = 1
        contadorElementos = 0
        contadorBasico = 0
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
                contadorBasico += 1


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
                
                if contadorBasico == elementosPines:
                    contadorBasico = 0
                    contadorPin += 1
                
                
                #print(f"Elemento: {elemento}")
            


        for compuesto in root.findall(".//listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text

            contador = 0
            lista_Elementos = ListaSimple()
            for elementos in compuesto.findall("elementos/elemento"):
                elemento = elementos.text
                contador += 1
                
                lista_Elementos._agregar_final(elemento)

            listaElementos_temp = dataCompuesto(nombre, lista_Elementos, contador)
            lista_CompuestosElementos._agregar_final(listaElementos_temp)


                # #print(f"Nombre: {nombre}, Elemento: {elemento}")
                # (len(compuesto.findall("elementos/elemento")))
                

            

cargaArchivo()
# listaElementosNodo._recorrer_adelante()
# listaElementosNodo._size()

print("\n\n")

nodo_actual = lista_CompuestosElementos.primero
while nodo_actual != None:
    print(nodo_actual.dato.get_nombreCompuesto())
    nodo_actual = nodo_actual.siguiente
