
CALLE_100 = 'Calle 100'
grafo_dijkstra = {
    'Portal Americas':[('Banderas', 1)],
    'Banderas':[('Puente Aranda',1)],
    'Puente Aranda':[('Ricaurte',1)],
    'Ricaurte':[('Av. Jimenez',1),(CALLE_100,6)],
    'Av. Jimenez':[('Calle 39',1)],
    'Calle 39':[('Flores',1)],
    'Flores':[(CALLE_100,1)],
    CALLE_100:[('Mazuren',1)],
    'Mazuren':[('Portal Norte',1)]
}