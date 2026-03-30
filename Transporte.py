from collections import deque
from grafo import grafo

#Punto de partida y destino
punto_a = 'Portal Americas'
punto_b = 'Portal Norte'

#Cola (FIFO) vacia para almacenar el camino completo hasta cada estacion
cola = deque([[punto_a]])

# Lista para alamcenar las estaciones recorridas
recorridas = set()

ruta_realizada = []

#Condicion del algoritmo para recorrido del grafo
# Utilizamos la busqueda BFS en anchura, cola primero en entrar, primero en salir
while cola:
#sacar de la cola
    camino = cola.popleft()
    estacion_actual = camino[-1]
    ruta_realizada.append(estacion_actual)

    print("Validando estacion actual: ", estacion_actual)

    if estacion_actual == punto_b:
        print("¡Sí, hemos llegado al destino!")
        print("Recorrido realizado: ", ruta_realizada)
        print("Mejor ruta para tomar: ", camino)
        break
    else:
        print("Aun no, seguir buscando...")   

        for estacion in grafo[estacion_actual]:
            if estacion not in recorridas:
                cola.append(camino + [estacion])
                recorridas.add(estacion)
        


