from logica import *
from carga import *
from creacionXML import *
import graphviz


def generadorGrap(compuesto, maquina):
    
    # Lista de Colores
    codigos_asignados = {}
    colores_disponibles = ['red', 'orange', 'yellow', 'green', 'blue', 'brown', 'blac', 'pink', 'chartreuse', 'darkorchid1', 'deepskyblue', 'gold3', 'gold1', 'firebrick1', 'blueviolet', 'aquamarine']

    # Asignador de Colores
    def asignar_color(codigo):
        if codigo in codigos_asignados:
            return codigos_asignados[codigo]
        color = colores_disponibles.pop(0)
        codigos_asignados[codigo] = color
        return color

    # logica, analiza el compuesto y la maquina para crear los pasos
    if logica(compuesto, maquina) != False:
        listaPasosGenerales, pasos = logica(compuesto, maquina)
        listaPasos = listaPasosGenerales
        contadorPasos = pasos
        #cantidadPasos = pasos
        #print(listaPasosGenerales._size())
        
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
            
        def encontradoPin(pin, lista):
            encontrado = False
            blabla = lista.dato.listaEspecificos.primero
            while blabla != None:
                if blabla.dato.pin == pin:
                    encontrado = True
                blabla = blabla.siguiente

            return encontrado

        
        with open("Reportes/pasos.dot", "w") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Pasos para fusionar: {compuesto}", labelloc=top]\n')
            grafo_dot.write('rankdir = TB \n' )
            grafo_dot.write(f'node[shape=box, style="filled" fontname="Arial", fontsize=12, fontcolor="black"] \n\n')

            contador = 0
            cantidadPines = 0
            nodo_general = listaPasos.primero
            while nodo_general != None:
                contador += 1
                nodo_especifico = nodo_general.dato.listaEspecificos.primero
                #print("siguiente \n")
                while nodo_especifico != None:
                    pin = nodo_especifico.dato.pin

                    if contador == 1:
                        cantidadPines += 1
                        grafo_dot.write(f'Paso{contador-1}_Pin{nodo_especifico.dato.pin} -> Paso{contador}_Pin{nodo_especifico.dato.pin} [label="Segundo: {contador}", fontname="Arial Black", fontsize=10] \n')
                        grafo_dot.write(f'Paso{contador-1}_Pin{nodo_especifico.dato.pin}[label="Pin Numero: {nodo_especifico.dato.pin}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}", fontsize="11", fontname="Arial Black"]\n\n')
                    
                    grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin} -> Paso{contador+1}_Pin{nodo_especifico.dato.pin} [label="Segundo: {contador+1}", fontname="Arial Black", fontsize=10] \n')
                    
                    terminado = nodo_general.siguiente
                    if encontradoPin(pin, terminado) == False:
                        grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin}[label="{movimiento(nodo_especifico.dato.movimiento, nodo_especifico.dato.elemento)} \nPosicion: {nodo_especifico.dato.posicion}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}"]\n\n')
                        grafo_dot.write(f'Paso{contador+1}_Pin{nodo_especifico.dato.pin}[label="Fin movimientos"]\n\n')
                    
                    else:
                        grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin}[label="{movimiento(nodo_especifico.dato.movimiento, nodo_especifico.dato.elemento)} \nPosicion: {nodo_especifico.dato.posicion}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}"]\n\n')
                    nodo_especifico = nodo_especifico.siguiente
                nodo_general = nodo_general.siguiente


            grafo_dot.write('\n\n}')

        generarXML(compuesto, maquina, listaPasos, contadorPasos)
        os.system("dot.exe -Tpdf Reportes/pasos.dot -o  Reportes/pasos.pdf")



    else:
        with open("Reportes/pasos.dot", "w") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Lista de Maquinas", labelloc=top]\n')
            grafo_dot.write('rankdir = TB \n' )
            grafo_dot.write(f'node[shape=box, style="filled" fontname="Arial", fontsize=12, fontcolor="black"] \n\n')
            grafo_dot.write('\n\n}')

        os.system("dot.exe -Tpdf Reportes/pasos.dot -o  Reportes/pasos.pdf")
        generarXMLError()
        print("Existe un error en el compuesto o sus elementos")
        return 404
    

def reporteMaquinas():

    listaMaquinas = get_listaMaquinas()

    nodo_actual = listaMaquinas.primero
    if nodo_actual != None:
        contador = 0
        with open("Reportes/maquinas.dot", "w") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Lista de Maquinas", labelloc=top]\n')
            grafo_dot.write('rankdir = LR \n' )
            grafo_dot.write('ranksep=1.5 \n' )
            grafo_dot.write(f'node[shape=none, style="filled" fontname="Arial", fontsize=12] \n\n')
            

            while nodo_actual != None:
                contador += 1
                grafo_dot.write(f'''
n{contador} [ label = <
    <table>
        <tr><td colspan="3" bgcolor="#245953" > <font color="white"> Maquina: {contador} </font></td></tr>
        <tr><td bgcolor="#408E91"> Nombre: {nodo_actual.dato.nombreMaquina} </td><td bgcolor="#E49393">Numero de Pines: {nodo_actual.dato.numeroDePines} </td><td bgcolor="#D8D8D8">Numero de Elementos: {nodo_actual.dato.numeroDeElementos} </td></tr>
                ''')

                nodo_pines = nodo_actual.dato.listaPines.primero
                while(nodo_pines != None):
                    nodo_elementos = nodo_pines.dato.listaPin.primero
                    while(nodo_elementos != None):
                        grafo_dot.write(f'''        
        <tr><td bgcolor="#6096B4"> Numero Pin: {nodo_pines.dato.contadorPin} </td><td bgcolor="#93BFCF"> Elemento: {nodo_elementos.dato.elementoPin} </td><td bgcolor="#BDCDD6">No. Elemento en Pin: {nodo_elementos.dato.contadorElemento} </td></tr>                
                        ''')
                        nodo_elementos = nodo_elementos.siguiente
                    nodo_pines = nodo_pines.siguiente
                

                grafo_dot.write(f'''
    </table>
> ]
                ''')
                nodo_actual = nodo_actual.siguiente 

            grafo_dot.write('\n\n}')
        os.system("dot.exe -Tpdf Reportes/maquinas.dot -o  Reportes/maquinas.pdf")
        return 100
    
    else:
        with open("Reportes/maquinas.dot", "w") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Existe en un error en las maquinas, o no ha cargado ningun archivo, Verifique :)", labelloc=top]\n')
            grafo_dot.write('rankdir = TB \n' )
            grafo_dot.write(f'node[shape=box, style="filled" fontname="Arial", fontsize=12, fontcolor="black"] \n\n')
            grafo_dot.write('\n\n}')

        os.system("dot.exe -Tpdf Reportes/maquinas.dot -o  Reportes/maquinas.pdf")
        print("Existe un error en el compuesto o sus elementos")
        return 404