from collections import deque


grafo = {
    'Portal Americas': ['Banderas'], 
    'Banderas': ['Puente Aranda'],
    'Puente Aranda': ['Ricaurte'],
    'Ricaurte':['Av. Jimenez','Calle 75'],
    'Calle 75': ['Calle 100'],
    'Av. Jimenez': ['Calle 39'],
    'Calle 39' : ['Flores'],
    'Flores': ['Calle 100'],
    'Calle 100' : ['Mazuren'],
    'Mazuren': ['Portal Norte']
}