import random

def GRASP(grafo, inicio, fin, max_iterations=100, alpha=0.5):
    mejorCamino = None
    mejorDistancia = float('inf')
    
    for i in range(max_iterations):
        Camino = OpcionCamino(grafo, inicio, fin, alpha)
        DistanciaTemp = Distancia_Camino(grafo, Camino)
        if DistanciaTemp < mejorDistancia:
            mejorCamino = Camino
            mejorDistancia = DistanciaTemp
        
    return mejorCamino, mejorDistancia

def OpcionCamino(grafo, inicio, fin, alpha):
    camino = [inicio]
    NodoActual = inicio
    
    while NodoActual != fin:
        vecinos = ObtenerVecinos(grafo, NodoActual)
        vecinosDisponibles = []
        distanciaMin = float('inf')
        
        for Vecino, Distancia in vecinos:
            if Vecino not in camino:
                vecinosDisponibles.append((Vecino, Distancia))
                if Distancia < distanciaMin:
                    distanciaMin = Distancia
        
        DistanciaLimite = distanciaMin + alpha * (Mejor_camino_al_Destino(grafo, NodoActual, fin) - distanciaMin)
        vecinosPosibles = [Vecino for Vecino, Distancia in vecinosDisponibles if Distancia <= DistanciaLimite]
        
        if not vecinosPosibles:
            return None
        
        vecinoElegido = random.choice(vecinosPosibles)
        camino.append(vecinoElegido)
        NodoActual = vecinoElegido
        
    return camino

def ObtenerVecinos(grafo, nodo):
    return grafo[nodo]

def Mejor_camino_al_Destino(grafo, nodo, fin):
    Distancias = {nodo: 0}
    cola = [nodo]
    
    while cola:
        NodoActual = cola.pop(0)
        if NodoActual == fin:
            return Distancias[fin]
        
        for vecino, Distancia in ObtenerVecinos(grafo, NodoActual):
            if vecino not in Distancias:
                Distancias[vecino] = Distancias[NodoActual] + Distancia
                cola.append(vecino)
                
    return float('inf')

def Distancia_Camino(grafo, camino):
    Distancia = 0
    for i in range(len(camino) - 1):
        vecinos = ObtenerVecinos(grafo, camino[i])
        for vecino, DistanciaLimite in vecinos:
            if vecino == camino[i+1]:
                Distancia += DistanciaLimite
    return Distancia




grafo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 5), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

inicio = 'A'
fin = 'D'
camino, Distancia = GRASP(grafo, inicio, fin)

if camino is None:
    print(f"No path found from {inicio} to {fin}.")
else:
    print(f"Shortest path from {inicio} to {fin}: {camino}.")
    print(f"Distancia: {Distancia}.")
