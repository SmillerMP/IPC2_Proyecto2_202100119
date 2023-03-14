import xml.etree.ElementTree as ET



# listaCelulas = lista()


# def get_listaCelulas():
#     return listaCelulas



def cargaArchivo():
    ruta = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\prueba.xml"
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

        if (len(listaElementos) != (cantidadElementos*numeroPines)):
            ListaElemetosError.append(contador)

    #print(ListaElemetosError)



    if (len(ListaPinError) != 0):
        print("Existe Error con los PINES del XML en las Siguientes Maquinas: ")
        for x in ListaPinError:
            print(f"Maquina: {x}")

    elif (len(ListaElemetosError) != 0): 
        print("Existe Error con los ELEMENTOS del XML en las Siguientes Maquinas: ")
        for x in ListaElemetosError:
            print(f"Maquina: {x}")

    else:
        for elemento in root.findall(".//listaElementos/elemento"):
            numeroAtomico = elemento.find("numeroAtomico").text
            simbolo = elemento.find("simbolo").text
            nombreElemento = elemento.find("nombreElemento").text
            
            print(f"Numero Atomico: {numeroAtomico}, Simbolo: {simbolo}, Nombre Elemento: {nombreElemento}")


        for Maquina in root.findall(".//listaMaquinas/Maquina"):
            nombre = Maquina.find("nombre").text
            numeroPines = Maquina.find("numeroPines").text
            numeroElementos = Maquina.find("numeroElementos").text
            

            print(f"Nombre: {nombre}, Numero Pines: {numeroPines}, Numero Elementos: {numeroElementos}")
            contadorPines = 0

            for elementos in Maquina.findall("pin/elementos/elemento"):
                elemento = elementos.text
                contadorPines += 1

                
                print(f"Elemento: {elemento}")
            


        for compuesto in root.findall(".//listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text


            for elementos in compuesto.findall("elementos/elemento"):
                elemento = elementos.text

                print(f"Nombre: {nombre}, Elemento: {elemento}")

            

cargaArchivo()