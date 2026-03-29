from grafo import grafo

punto_a = 'Portal Americas'
punto_b = 'Portal Norte'

#PILA (LIFO) vacia para almacenar los puntos recorridos
pila = [punto_a]

# Lista para alamcenar las estaciones recorridas
recorridas = set()

ruta_realizada = []

#Condicion del algoritmo para recorrido del grafo
# Utilizamos la busqueda BFS en anchura, cola primero en entrar, primero en salir
while pila:

    estacion_actual = pila.pop()
    ruta_realizada.append(estacion_actual)

    print("Validando estacion actual: ", estacion_actual)

    if estacion_actual == punto_b:
        print("¡Sí, hemos llegado al destino!")
        print("Recorido realizado: ", ruta_realizada)
        break
    else:
        print("Aun no, seguir buscando...")   

        for estacion in grafo[estacion_actual]:
            if estacion not in recorridas:
                pila.append(estacion)
                recorridas.add(estacion)