import xml.etree.ElementTree as ET



# listaCelulas = lista()


# def get_listaCelulas():
#     return listaCelulas



def cargaArchivo():
    ruta = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\prueba.xml"
    tree = ET.parse(ruta)
    root = tree.getroot()


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

        for elementos in Maquina.findall("pin/elementos/elemento"):
            elemento = elementos.text

            
            print(f"Elemento: {elemento}")




    for compuesto in root.findall(".//listaCompuestos/compuesto"):
        nombre = compuesto.find("nombre").text


        for elementos in compuesto.findall("elementos/elemento"):
            elemento = elementos.text

            print(f"Nombre: {nombre}, Elemento: {elemento}")

            

cargaArchivo()