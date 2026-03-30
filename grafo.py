
CALLE_100= 'Calle 100'

grafo = {
    'Portal Americas': ['Banderas'], 
    'Banderas': ['Puente Aranda'],
    'Puente Aranda': ['Ricaurte'],
    'Ricaurte':['Av. Jimenez','Calle 75'],
    'Calle 75': [CALLE_100],
    'Av. Jimenez': ['Calle 39'],
    'Calle 39' : ['Flores'],
    'Flores': [CALLE_100],
    CALLE_100 : ['Mazuren'],
    'Mazuren': ['Portal Norte']
}