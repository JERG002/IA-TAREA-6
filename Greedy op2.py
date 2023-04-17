import random
import time
import Ponderado as GRP
import GRASP as Grasp


def generador_grafo(nodos):
    instancia = {}
    for i in range(1,nodos+1):
        nodos_adyacentes = random.randint(2, nodos-1)
        lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        while(i in lista_nodos_adyacentes):
            nodos_adyacentes = random.randint(2,nodos-1)
            lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        
        lista_tuplas = []
        for j in range(0, len(lista_nodos_adyacentes)):
            lista_tuplas.append((str(lista_nodos_adyacentes[j]),random.randint(1,1000)))
        instancia[str(i)] = lista_tuplas


    for i in instancia:
        valida = 0    
        for j in instancia[i]:
            for x in instancia:
                JJ = -1
                for y in instancia[x]:
                    JJ = JJ + 1
                    if x != i:
                        if i == instancia[x][JJ][0]:
                            valida = 1
        if valida == 0:
            insertar  = str(random.randint(1, nodos))
            tupla_insertada = (i, random.randint(1,1000))
            while i == insertar:
                insertar  = str(random.randint(1, nodos))
            instancia[insertar].insert(0,tupla_insertada)

    return instancia

CantidadNodos = 50 

inicial  = str(random.randint(1, CantidadNodos))
final  = str(random.randint(1, CantidadNodos))
while inicial == final:
    inicial  = str(random.randint(1, CantidadNodos))
    final  = str(random.randint(1, CantidadNodos))

grafo = generador_grafo(CantidadNodos)
#G= nx.complete_graph(grafo)
#nx.draw_circular(G, node_size= len(grafo), width=1, width_label=False)
#plt.axes("equals")
#plt.show()

g = GRP.WeightedGraph(grafo)

print("Grafo : ", grafo)

inicio = time.time()
print(f"Inicio: {inicial}, final: {final}")


#ALGORITMO DE DIJKSTRA      -----------------------------------------------------------------------------------------------
path, weight = g.shortestPath(inicial,final)
print(f'Dijkstra: ruta: {path} peso: {weight}')

fin = time.time()
print('Tiempo de ejecucion Dijkstra: ', fin-inicio)
#--------------------------------------------------------------------------------------------------------------------------


#GRASP---------------------------------------------------------------------------------------------------------------------
inicio = time.time()
ruta, peso = Grasp.GRASP(grafo, inicial, final)
print(f'GRASP: ruta: {path} peso: {weight}')

fin = time.time()
print('Tiempo de ejecucion GRASP: ', fin-inicio)
#--------------------------------------------------------------------------------------------------------------------------
