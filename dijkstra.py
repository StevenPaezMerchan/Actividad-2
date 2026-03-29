#Importar para la cola de prioridad
import heapq
#Importar el grafo con valores(peso)
from grafo_dijkstra import grafo_dijkstra
#Variables de puntos inicial y punto final
punto_a = 'Portal Americas'
punto_b = 'Portal Norte'
#1. Lista de prioridad vacia para usar heapq, 2. agrergar el punto de inicio con peso 0
cola_principal = []
heapq.heappush(cola_principal,(0,punto_a))
#Set vacio para almacenar el recorrido de las estaciones
recorrido = set()
#Lista vacia para guardar el recorrido
ruta_recorrida = []

#Condicion del algoritmo para recorrido del grafo
while cola_principal:
    #Sacar el peso y la estacion actual de la cola de prioridad
    peso_actual, estacion_actual = heapq.heappop(cola_principal)

    if estacion_actual in recorrido:
        continue
    else:
        recorrido.add(estacion_actual)
        ruta_recorrida.append(estacion_actual)
        if estacion_actual == punto_b:
            print("¡Sí, hemos llegado al destino!")
            print("El peso actual: ", peso_actual)
            print("Recorido realizado: ", ruta_recorrida)
            break

        for vecino in grafo_dijkstra[estacion_actual]:
            nuevo_peso = peso_actual + vecino[1]
            heapq.heappush(cola_principal,(nuevo_peso, vecino[0]) )