from logica import *
from carga import *
import graphviz


codigos_asignados = {}
colores_disponibles = ['red', 'orange', 'yellow', 'green', 'blue', 'brown', 'blac', 'pink', 'chartreuse', 'darkorchid1', 'deepskyblue', 'gold3', 'gold1', 'firebrick1', 'blueviolet', 'aquamarine']

def asignar_color(codigo):
    if codigo in codigos_asignados:
        return codigos_asignados[codigo]
    color = colores_disponibles.pop(0)
    codigos_asignados[codigo] = color
    return color

rutaInfo = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\Archivos de prueba\\entrada_proyecto2_dummy.xml"
rutaloca = "D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\IPC 2\\Proyectos IPC2\\IPC2_Proyecto2_202100119\\IPC2_Proyecto2_202100119\\Archivos de prueba\\prueba.xml"
cargaArchivo(rutaInfo)
Compuesto = "Energon"
maquina = "prueba"
if logica(Compuesto, maquina) != False:
    listaPasosGenerales = logica(Compuesto, maquina)
    print(listaPasosGenerales._size())

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
        grafo_dot.write(f'graph [label="Pasos para fusionar: {Compuesto}", labelloc=top]\n')
        grafo_dot.write('rankdir = TB \n' )
        grafo_dot.write(f'node[shape=box, style="filled" fontname="Arial", fontsize=12, fontcolor="black"] \n\n')



        contador = 0
        cantidadPines = 0
        nodo_general = listaPasosGenerales.primero
        while nodo_general != None:
            contador += 1
            nodo_especifico = nodo_general.dato.listaEspecificos.primero
            print("siguiente \n")
            while nodo_especifico != None:
                pin = nodo_especifico.dato.pin

                if contador == 1:
                    cantidadPines += 1
                    grafo_dot.write(f'Paso{contador-1}_Pin{nodo_especifico.dato.pin} -> Paso{contador}_Pin{nodo_especifico.dato.pin} [label="Paso: {contador}"]\n')
                    grafo_dot.write(f'Paso{contador-1}_Pin{nodo_especifico.dato.pin}[label="Pin Numero: {nodo_especifico.dato.pin}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}", fontsize="11", fontname="Arial Black"]\n\n')
                
                grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin} -> Paso{contador+1}_Pin{nodo_especifico.dato.pin} [label="Paso: {contador+1}"] \n')
                
                terminado = nodo_general.siguiente
                if encontradoPin(pin, terminado) == False:
                    grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin}[label="{movimiento(nodo_especifico.dato.movimiento, nodo_especifico.dato.elemento)}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}"]\n\n')
                    grafo_dot.write(f'Paso{contador+1}_Pin{nodo_especifico.dato.pin}[label="Fin movimientos"]\n\n')
                
                else:
                    grafo_dot.write(f'Paso{contador}_Pin{nodo_especifico.dato.pin}[label="{movimiento(nodo_especifico.dato.movimiento, nodo_especifico.dato.elemento)}", fillcolor="{asignar_color(nodo_especifico.dato.pin)}"]\n\n')
                nodo_especifico = nodo_especifico.siguiente
            nodo_general = nodo_general.siguiente


        grafo_dot.write('\n\n}')

    os.system("dot.exe -Tpdf Reportes/pasos.dot -o  Reportes/pasos.pdf")

else:
    with open("Reportes/pasos.dot", "w") as grafo_dot:
        grafo_dot.write('digraph { \n')
        grafo_dot.write(f'graph [label="Error en el archivo XML o en la seleccion, verifique por favor", labelloc=top]\n')
        grafo_dot.write('rankdir = TB \n' )
        grafo_dot.write(f'node[shape=box, style="filled" fontname="Arial", fontsize=12, fontcolor="black"] \n\n')
        grafo_dot.write('\n\n}')

    os.system("dot.exe -Tpdf Reportes/pasos.dot -o  Reportes/pasos.pdf")
    print("Existe un error en el compuesto o sus elementos")