# Línea 1: Descomponiendo len(), range(), y list() para "CETPRO PUNO"
longitud_cadena = len("CETPRO PUNO")  # len() calcula la longitud de la cadena
rango_cadena = range(longitud_cadena)  # range() genera la secuencia de números
lista_cadena = list(rango_cadena)  # list() convierte el rango en una lista
print(lista_cadena)  # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Línea 2: Descomponiendo len(), range(), y list() para ["a","b","c"]
longitud_lista = len(["a", "b", "c"])  # len() calcula la longitud de la lista
rango_lista = range(longitud_lista)  # range() genera la secuencia de números
lista_lista = list(rango_lista)  # list() convierte el rango en una lista
print(lista_lista)  # Imprime: [0, 1, 2]

# Línea 3: Descomponiendo len(), range(), y list() para range(1, 100, 7)
rango_inicial = range(1, 100, 7)  # range() genera la secuencia 1, 8, 15, ..., 99
longitud_rango = len(rango_inicial)  # len() calcula la longitud del rango (15)
print(f"Una lista: {list(rango_inicial)} con longitud {longitud_rango}")  # list() convierte el rango inicial en lista, y se imprime con su longitud
