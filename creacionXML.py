import xml.etree.ElementTree as ET
import xml.dom.minidom

def generarXML(compuestoExperimento, maquinaExperimento, listaPasos, pasos):

    def movimiento(move, elemento):
        if move == 0:
            return "Esperar"
        elif move == 1:
            return "Mover Adelante"
        elif move == 2:
            return "Mover Atras"
        elif move == 3:
            retorno = "Fusionar Elemento: " + str(elemento)
            return retorno
        

    # Crea el elemento raíz del árbol XML
    root = ET.Element("RESPUESTA")

    # Crea el elemento listaCompuestos y lo agrega al elemento raíz
    lista_compuestos = ET.SubElement(root, "listaCompuestos")

    # Crea un elemento compuesto y lo agrega a la listaCompuestos
    compuesto = ET.SubElement(lista_compuestos, "compuesto")

    # agrega el elementos nombre al XML con el nombre del compuesto
    nombre = ET.SubElement(compuesto, "nombre")
    nombre.text = compuestoExperimento

    # Agrega un elemento maquina con el nombre de la Maquina
    maquina = ET.SubElement(compuesto, "maquina")
    maquina.text = maquinaExperimento

    # Agrega un elemento tiempoOptimo con su valor numérico al compuesto
    tiempo_optimo = ET.SubElement(compuesto, "tiempoOptimo")
    pasosStr = str(pasos)
    tiempo_optimo.text = pasosStr + " Segundos"

    # Crea el elemento instrucciones y lo agrega al compuesto
    instrucciones = ET.SubElement(compuesto, "instrucciones")


    contador = 0
    nodo_actual = listaPasos.primero
    while nodo_actual != None:
        contador += 1


        
        # Agrega un elemento tiempo con un sub-elemento numeroSegundo y un sub-elemento acciones al elemento instrucciones
        tiempo = ET.SubElement(instrucciones, "tiempo")
        numero_segundo = ET.SubElement(tiempo, "numeroSegundo")
        contadroStr = str(contador)
        numero_segundo.text = contadroStr
        acciones = ET.SubElement(tiempo, "acciones")

        nodo_especifico = nodo_actual.dato.listaEspecificos.primero
        while nodo_especifico != None:
            
            

            # Agrega un elemento accionPin con un sub-elemento numeroPin y un sub-elemento accion al elemento acciones
            accion_pin = ET.SubElement(acciones, "accionPin")
            numero_pin = ET.SubElement(accion_pin, "numeroPin")
            pinStr = str(nodo_especifico.dato.pin)
            numero_pin.text = pinStr
            accion = ET.SubElement(accion_pin, "accion")
            accion.text = movimiento(nodo_especifico.dato.movimiento, nodo_especifico.dato.elemento)

            nodo_especifico = nodo_especifico.siguiente

        nodo_actual = nodo_actual.siguiente

        if nodo_actual.siguiente == None:
            break


    # Crea el objeto ElementTree y escribe el árbol XML en un archivo
    doc = xml.dom.minidom.parseString(ET.tostring(root))
    with open('Reportes/reportePasos.xml', 'w') as archivo:
        archivo.write(doc.toprettyxml())



def generarXMLError():
    root = ET.Element("RESPUESTA")
    experimento = ET.SubElement(root, "experimento")
    experimento.text = "Error"
    
    doc = xml.dom.minidom.parseString(ET.tostring(root))
    with open('Reportes/reportePasos.xml', 'w') as archivo:
        archivo.write(doc.toprettyxml())